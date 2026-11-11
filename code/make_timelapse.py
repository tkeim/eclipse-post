"""Build a time-lapse of first graders' eclipse drawings (Boulder, 2017-08-21).
Crops off the name/header block, adds time + computed % of Sun covered + coverage curve."""
import glob, re, io, sys, os, numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from skyfield.api import load, load_file, wgs84

TIMES = ['10:32','10:32','10:32','10:40','10:40','10:40','10:47','10:52','10:55','10:55','11:00',
         '11:05','11:08','11:12','11:12','11:15','11:20','11:20','11:25','11:40','11:50','12:05']
# usage: python code/make_timelapse.py <folder of scanned drawings>
SRC = sys.argv[1] if len(sys.argv) > 1 else 'timeLapseDrawings'
fs = sorted(glob.glob(os.path.join(SRC, 'Doc*.png')),
            key=lambda f: int(re.search(r'-(\d+)\.png', f).group(1)))
assert len(fs) == len(TIMES)

# --- eclipse geometry for Boulder, every minute 10:15-13:20 MDT (UTC-6)
eph = load_file('de421.bsp'); ts = load.timescale()
obs = eph['earth'] + wgs84.latlon(40.015, -105.27)
mins = np.arange(10*60+15, 13*60+21)
t = ts.utc(2017, 8, 21, 6, mins)          # hour 6 + local minutes = UTC
s = obs.at(t).observe(eph['sun']).apparent(); m = obs.at(t).observe(eph['moon']).apparent()
x = s.separation_from(m).radians
r1 = np.arcsin(696000/s.distance().km); r2 = np.arcsin(1737.4/m.distance().km)
a1 = r1**2*np.arccos(np.clip((x*x+r1*r1-r2*r2)/(2*x*r1), -1, 1))
a2 = r2**2*np.arccos(np.clip((x*x+r2*r2-r1*r1)/(2*x*r2), -1, 1))
a3 = .5*np.sqrt(np.clip((-x+r1+r2)*(x+r1-r2)*(x-r1+r2)*(x+r1+r2), 0, None))
cov = np.where(x < r1+r2, (a1+a2-a3)/(np.pi*r1*r1), 0)*100
def cov_at(hhmm):
    h, mm = map(int, hhmm.split(':')); return float(np.interp(h*60+mm, mins, cov))
print('max %.1f%% at %d:%02d' % (cov.max(), *divmod(mins[cov.argmax()], 60)))

FW, FH = 1000, 1250                      # frame size
DRAW_H = 900
font_big = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 48)
font_sm = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 26)

def curve_png(hhmm):
    fig, ax = plt.subplots(figsize=(9.6, 2.4), dpi=100)
    hrs = mins/60
    ax.fill_between(hrs, cov, color='#f2a33a', alpha=.25, lw=0)
    ax.plot(hrs, cov, color='#c4651a', lw=2)
    for tt in TIMES:
        h, mm = map(int, tt.split(':')); ax.plot(h+mm/60, cov_at(tt), 'o', ms=4, color='#999')
    h, mm = map(int, hhmm.split(':')); ax.plot(h+mm/60, cov_at(hhmm), 'o', ms=14, color='#1f3b73')
    ax.set_xlim(hrs[0], hrs[-1]); ax.set_ylim(0, 100)
    ax.set_xticks([10.5, 11, 11.5, 12, 12.5, 13]); ax.set_xticklabels(['10:30','11:00','11:30','12:00','12:30','1:00'])
    ax.set_yticks([0, 50, 100]); ax.set_yticklabels(['0%','50%','100%'])
    for sp in ['top', 'right']: ax.spines[sp].set_visible(False)
    ax.set_ylabel('Sun covered', fontsize=11)
    fig.tight_layout(); b = io.BytesIO(); fig.savefig(b, format='png'); plt.close(fig)
    return Image.open(b).convert('RGB')

frames = []
for f, hhmm in zip(fs, TIMES):
    im = Image.open(f).convert('RGB'); W, H = im.size
    d = im.crop((0, int(.235*H), W, int(.975*H)))          # drop name/date/time header
    d.thumbnail((FW-40, DRAW_H))
    fr = Image.new('RGB', (FW, FH), 'white')
    fr.paste(d, ((FW-d.size[0])//2, 10))
    g = ImageDraw.Draw(fr)
    h, mm = map(int, hhmm.split(':'))
    label = f'{h}:{mm:02d} {"AM" if h < 12 else "PM"}'
    g.text((40, DRAW_H+12), label, font=font_big, fill='#1f3b73')
    g.text((330, DRAW_H+28), f'{cov_at(hhmm):.0f}% of the Sun covered', font=font_sm, fill='#333')
    c = curve_png(hhmm); fr.paste(c, ((FW-c.size[0])//2, FH-c.size[1]-5))
    frames.append(fr)

os.makedirs('build_frames', exist_ok=True)
for k, fr in enumerate(frames): fr.save(f'build_frames/f{k:02d}.png')
print([f'{tt} {cov_at(tt):.0f}%' for tt in TIMES])

# Encode (run from the project root):
#   ffmpeg -framerate 1/1.2 -i build_frames/f%02d.png -vf "fps=25,format=yuv420p" -c:v libx264 -preset veryfast -crf 23 -movflags +faststart images/eclipse_drawings_timelapse.mp4
#   ffmpeg -framerate 1/1.2 -i build_frames/f%02d.png -vf "fps=5,scale=560:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=96[p];[b][p]paletteuse=dither=bayer:bayer_scale=4" -loop 0 images/eclipse_drawings_timelapse.gif
