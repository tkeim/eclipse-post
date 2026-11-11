"""Solar eclipses visible from Boulder, CO: start, maximum, end, coverage.
Geometry: Skyfield + DE421, topocentric disks, 1-minute steps. "Sun up" uses the
standard sunrise/sunset altitude (-0.833 deg: upper limb plus refraction).
Coverage is the fraction of the Sun's disk area covered (same as eclipse_pop.py).
Usage: python code/boulder_eclipses.py [start_year] [end_year]
"""
import sys
from zoneinfo import ZoneInfo
import numpy as np
from skyfield.api import load, load_file, wgs84
from skyfield import almanac

ts = load.timescale()
eph = load_file('de421.bsp')
earth, sun, moon = eph['earth'], eph['sun'], eph['moon']
R_SUN, R_MOON = 696000.0, 1737.4
BOULDER = wgs84.latlon(40.015, -105.27)
TZ = ZoneInfo('America/Denver')


def overlap_frac(rs, rm, d):
    """Fraction of solar disk area covered by lunar disk (all angles, radians)."""
    out = np.zeros_like(d)
    full = d <= rm - rs
    out[full] = 1.0
    inside = (d <= rs - rm) & ~full
    out[inside] = (rm[inside] / rs[inside]) ** 2
    part = (d < rs + rm) & ~full & ~inside
    r1, r2, dd = rs[part], rm[part], d[part]
    a1 = r1**2 * np.arccos(np.clip((dd**2 + r1**2 - r2**2) / (2*dd*r1), -1, 1))
    a2 = r2**2 * np.arccos(np.clip((dd**2 + r2**2 - r1**2) / (2*dd*r2), -1, 1))
    a3 = 0.5*np.sqrt(np.clip((-dd+r1+r2)*(dd+r1-r2)*(dd-r1+r2)*(dd+r1+r2), 0, None))
    out[part] = (a1 + a2 - a3) / (np.pi * r1**2)
    return out


def local(t):
    return t.utc_datetime().astimezone(TZ)


y0, y1 = (int(a) for a in sys.argv[1:3]) if len(sys.argv) > 2 else (2026, 2050)
tt, ph = almanac.find_discrete(ts.utc(y0, 1, 1), ts.utc(y1 + 1, 1, 1), almanac.moon_phases(eph))
here = earth + BOULDER

for nm in tt[ph == 0]:
    t = ts.tt_jd(nm.tt + np.arange(-300, 301) / 1440.0)   # +/-5 h, 1-min steps
    s = here.at(t).observe(sun).apparent()
    m = here.at(t).observe(moon).apparent()
    alt = s.altaz()[0].degrees
    d = s.separation_from(m).radians
    rs = np.arcsin(R_SUN / s.distance().km)
    rm = np.arcsin(R_MOON / m.distance().km)
    f = np.where(alt > -0.833, overlap_frac(rs, rm, d), 0.0)
    on = np.nonzero(f > 0)[0]
    if len(on) == 0:
        continue
    i0, i1, imax = on[0], on[-1], np.argmax(f)
    begin = local(t[i0]).strftime('%I:%M %p') + (' (sunrise)' if alt[i0 - 1] <= -0.833 else '')
    end = local(t[i1]).strftime('%I:%M %p') + (' (sunset)' if alt[i1 + 1] <= -0.833 else '')
    mins = i1 - i0
    print(f"{local(t[imax]):%a %Y-%m-%d}  max {f[imax]:4.0%} at {local(t[imax]):%I:%M %p}  "
          f"{begin} to {end}  ({mins // 60} h {mins % 60:02d} min)")
