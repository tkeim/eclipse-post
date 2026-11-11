# Partial Eclipses >> Total Eclipses

A short blog post (and companion to a 5-minute lightning talk) arguing that partial eclipses are underrated: they reach far more people, last for hours, and are a perfect low-budget science activity.

## Build the site

```bash
npm install -g mystmd      # once
myst start                 # live preview at http://localhost:3000
myst build --html          # static site in _build/html
```

## Publish to GitHub Pages

```bash
git init && git add . && git commit -m "First draft"
# create an empty repo on GitHub, then:
git remote add origin https://github.com/YOUR-USERNAME/eclipse-post.git
git push -u origin main
myst init --gh-pages       # writes .github/workflows/deploy.yml
git add .github && git commit -m "Deploy to GitHub Pages" && git push
```

Then in the repo on GitHub: Settings → Pages → Source: **GitHub Actions**.

## Layout

| Path | What |
|---|---|
| `index.md` | The post |
| `myst.yml` | MyST project config |
| `images/` | Photos (badge blurred, metadata stripped), map, time-lapse (MP4 + GIF) |
| `code/eclipse_pop.py` | Population with ≥X% eclipse coverage, Nov 2026–Nov 2031 |
| `code/boulder_eclipses.py` | Every eclipse visible from Boulder: times, coverage, duration |
| `code/make_timelapse.py` | Builds the first-grader drawings time-lapse |

## Re-running the numbers

```bash
pip install skyfield geonamescache numpy matplotlib pillow
curl -LO https://raw.githubusercontent.com/skyfielders/python-skyfield/master/ci/de421.bsp
python code/eclipse_pop.py
python code/make_timelapse.py "path/to/timeLapseDrawings"   # then see ffmpeg lines at the end of the script
```

The time-lapse script crops off the top of each scanned sheet so the children's names don't appear. Keep the raw scans out of the repo (they're in `.gitignore`).
