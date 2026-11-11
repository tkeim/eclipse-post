"""Population seeing >=X% solar obscuration, Nov 2026 - Nov 2031.
Geometry: Skyfield + DE421, topocentric disks, Sun above horizon.
Population: geonames cities >15k as a spatial sample, scaled to country totals.
"""
import numpy as np, geonamescache
from collections import defaultdict
from skyfield.api import load, load_file, wgs84
from skyfield import almanac
from skyfield.framelib import itrs

ts = load.timescale()
eph = load_file('de421.bsp')
earth, sun, moon = eph['earth'], eph['sun'], eph['moon']
AU_KM = 149597870.7
R_SUN, R_MOON = 696000.0, 1737.4

gc = geonamescache.GeonamesCache()
cities = list(gc.get_cities().values())
countries = gc.get_countries()
lat = np.array([c['latitude'] for c in cities])
lon = np.array([c['longitude'] for c in cities])
cpop = np.array([c['population'] for c in cities], float)
ccode = np.array([c['countrycode'] for c in cities])
obs_itrs = wgs84.latlon(lat, lon).itrs_xyz.km          # (3, N)
up_itrs = obs_itrs / np.linalg.norm(obs_itrs, axis=0)

# country scaling: each city stands for (country pop / sum of city pop in country)
city_sum = defaultdict(float)
for cc, p in zip(ccode, cpop): city_sum[cc] += p
weight = np.array([countries[cc]['population'] / city_sum[cc] if cc in countries else 1.0
                   for cc in ccode]) * cpop
weight = np.nan_to_num(weight, posinf=0.0)
WORLD = sum(v['population'] for v in countries.values())

def overlap_frac(rs, rm, d):
    """Fraction of solar disk area covered by lunar disk (all angles, radians)."""
    out = np.zeros_like(d)
    full = d <= rm - rs                     # total
    out[full] = 1.0
    inside = (d <= rs - rm) & ~full         # annular: moon entirely inside sun
    out[inside] = (rm[inside] / rs[inside]) ** 2
    part = (d < rs + rm) & ~full & ~inside
    r1, r2, dd = rs[part], rm[part], d[part]
    a1 = r1**2 * np.arccos(np.clip((dd**2 + r1**2 - r2**2) / (2*dd*r1), -1, 1))
    a2 = r2**2 * np.arccos(np.clip((dd**2 + r2**2 - r1**2) / (2*dd*r2), -1, 1))
    a3 = 0.5*np.sqrt(np.clip((-dd+r1+r2)*(dd+r1-r2)*(dd-r1+r2)*(dd+r1+r2), 0, None))
    out[part] = (a1 + a2 - a3) / (np.pi * r1**2)
    return out

t0, t1 = ts.utc(2026, 11, 11), ts.utc(2031, 11, 11)
tt, ph = almanac.find_discrete(t0, t1, almanac.moon_phases(eph))
new_moons = tt[ph == 0]

results = []
best_overall = np.zeros(len(cities))
for nm in new_moons:
    steps = np.arange(-240, 241, 3) / 1440.0      # +/-4 h, 3-min steps
    t = ts.tt_jd(nm.tt + steps)
    s = earth.at(t).observe(sun).apparent().position.km   # (3, T) GCRS
    m = earth.at(t).observe(moon).apparent().position.km
    R = itrs.rotation_at(t)                                # GCRS->ITRS, (3,3,T)
    # quick reject: geocentric separation too large for any eclipse
    geo_sep = np.arccos(np.sum(s*m, 0) / np.linalg.norm(s, axis=0) / np.linalg.norm(m, axis=0))
    if geo_sep.min() > np.radians(1.6):
        continue
    best = np.zeros(len(cities)); is_total = np.zeros(len(cities), bool)
    for k in range(len(steps)):
        Rk = R[:, :, k]
        o = Rk.T @ obs_itrs                     # observer in GCRS, (3,N)
        u = Rk.T @ up_itrs
        sv = s[:, k:k+1] - o; mv = m[:, k:k+1] - o
        ds, dm = np.linalg.norm(sv, axis=0), np.linalg.norm(mv, axis=0)
        up = np.sum(sv*u, 0) / ds > 0           # Sun above horizon
        d = np.arccos(np.clip(np.sum(sv*mv, 0)/ds/dm, -1, 1))
        rs, rm = np.arcsin(R_SUN/ds), np.arcsin(R_MOON/dm)
        f = np.where(up, overlap_frac(rs, rm, d), 0)
        is_total |= up & (d <= rm - rs)
        best = np.maximum(best, f)
    date = nm.utc_strftime('%Y-%m-%d')
    row = dict(date=date, any=weight[best > 0.001].sum(), p25=weight[best >= .25].sum(),
               p50=weight[best >= .5].sum(), p90=weight[best >= .9].sum(),
               total=weight[is_total].sum(), maxf=best.max())
    results.append(row)
    best_overall = np.maximum(best_overall, best)

print(f"World pop (geonames): {WORLD/1e9:.2f} B")
print(f"{'date':12}{'any':>9}{'>=25%':>9}{'>=50%':>9}{'>=90%':>9}{'total':>9}  (millions)")
for r in results:
    print(f"{r['date']:12}{r['any']/1e6:9.0f}{r['p25']/1e6:9.0f}{r['p50']/1e6:9.0f}{r['p90']/1e6:9.0f}{r['total']/1e6:9.1f}")
for thr in [0.001, .25, .5, .9]:
    w = weight[best_overall >= thr].sum()
    print(f"Union >= {thr:.0%}: {w/1e9:.2f} B = {w/WORLD:.0%} of world")
np.save('best_overall.npy', best_overall)
