---
title: Partial Eclipses >> Total Eclipses
subtitle: Get outside and do nerdy stuff
date: 2026-11-11
---

:::{figure} images/boulder_2017_crescents.jpg
:label: fig-crescents
:alt: Hundreds of crescent-shaped spots of sunlight on a white card in the grass, projected through the gaps in a tree's leaves

Boulder, Colorado, August 21, 2017. The Sun was about 93% covered.
:::

Total solar eclipses are spectacular. I'm not here to argue otherwise.

:::{figure} images/totality_nasa_2017.jpg
:label: fig-totality
:alt: The totally eclipsed Sun: a black lunar disk ringed by the glowing white corona, its streamers fanning out against a dark sky

Totality above Madras, Oregon, August 21, 2017, the same day as the Boulder photos in this post. Photo: [NASA/Aubrey Gemignani](https://www.eurekalert.org/multimedia/982260) (public domain).
:::

% Swap in once Mike Hay says yes (and remove images/totality_mike_hay.jpg from .gitignore):
% :::{figure} images/totality_mike_hay.jpg
% :label: fig-totality
% :alt: The totally eclipsed Sun: a black lunar disk ringed by the glowing white corona, with small pink prominences at the edge
%
% Totality, April 8, 2024. Photo © Mike Hay, used with permission.
% :::

Partial eclipses tickle my brain in a way totality does not. They are my favorite kind of science: outdoor, community science, with the whole neighborhood looking at the same Sun through whatever has holes in it. The accessibility is a part of their magic. You don't go to a partial eclipse; it comes to you, and it comes back every few years. They last far longer, cost nothing, and show you something totality never can: the shape of the Sun, printed on the ground a thousand times over by every gap in every tree.

## Totality is for travelers. Partials are for everyone.

:::{margin}
"I" = me and Claude.
:::

"I" estimated how many people will see each kind of eclipse from home in the next 5 years. Only about **1 in 80 people on Earth** lives in a path of totality, and most of them are in one eclipse: Spain, North Africa and the Middle East on August 2, 2027. Everyone else has to travel to totality. That means a plane ticket, a hotel booked a year or two ahead, time off work, and the luck of clear skies on one narrow strip of ground on one particular day. Most people can't do that.

Partials are different. Roughly **6 in 10 people on Earth** will get a deep partial eclipse without leaving home, compared with about 1 in 80 for totality.

:::{figure} images/coverage_infographic.png
:label: fig-people
:alt: Infographic titled "Partial solar eclipses, the next 5 years: 48 in 80 (6 in 10) can see a partial eclipse over 50% from home." A grid of 80 person icons: 1 dark gold for totality at home, 47 outlined for a partial over 50% at home, and 32 gray for less than that.
:::

## Totality lasts minutes. A partial lasts hours.

Totality lasts a few minutes at most. Even the "eclipse of the century" in August 2027 tops out around six minutes. Here's every eclipse visible from Boulder since 2010:

| Date | Max coverage | Peak (local time) | Duration |
|---|---|---|---|
| May 20, 2012 | 79% | 7:29 PM | 1 h 51 min, cut short by sunset |
| Oct 23, 2014 | 45% | 4:34 PM | 2 h 25 min |
| Aug 21, 2017 | 93% | 11:46 AM | 2 h 50 min |
| Oct 14, 2023 | 78% | 10:36 AM | 2 h 51 min |
| Apr 8, 2024 | 64% | 12:39 PM | 2 h 24 min |
| **Jan 14, 2029** (upcoming) | **64%** | **9:50 AM** | **2 h 57 min** |

Six partial eclipses in 17 years, five of them covering more than half the Sun, each lasting hours, not minutes. Total eclipses in Boulder over the same stretch: zero.

That's enough time to wander around, try things, call the neighbors over, and run actual experiments. Even with 6-year-olds.

## A time-lapse by first graders

In 2017 I ran an impromptu eclipse activity at my kid's elementary school. We had about 2 hours leading up to maximum, we brought kids outside in small groups, about 10 minutes at a time. Each kid looked through eclipse glasses and drew what they saw. The small groups enabled us to share the experience with all kids in the grade even though we only had a handful of eclipse glasses available. Near maximum eclipse, everyone came back out together.

Put the drawings in order and you get a time-lapse of the eclipse, observed and documented by first graders:

:::{figure} images/eclipse_drawings_timelapse.mp4
:label: fig-timelapse
:alt: Animated sequence of 22 children's drawings of the partially eclipsed Sun, from 10:32 AM to 12:05 PM, grouped by the time each was drawn and labeled with the calculated percentage of the Sun covered, above a curve of coverage through the morning

Boulder, August 21, 2017. Times are the ones the kids wrote on their sheets. The percentages and the curve are calculated for Boulder; maximum was 93% at 11:46 AM.
:::

They're not all scientifically accurate. One kid drew a smiling sun with rays. But the trend is unmistakable: the bite grows until the Sun is a thin sliver.

## Every gap is a pinhole camera

:::{figure} images/colander_pair_2017.jpg
:label: fig-colander
:alt: Two photos side by side. Left: an adult and a child holding a metal colander over a sidewalk; in its shadow, a card and the pavement are covered with small crescents. Right: the shadow of a person holding a colander; on a card in the colander's shadow, dozens of crescents are arranged in the colander's hole pattern.

**Left:** the setup: one kitchen colander, one helper, one index card. **Right:** the result. Each hole makes its own crescent, and together they reproduce the colander's hole pattern. The arrangement comes from the colander; the shape of each spot comes from the Sun.
:::

Every small gap, whether between leaves or in a colander, acts like a **pinhole camera**. The spot of light it throws on the ground isn't the shape of the gap. It's an image of the Sun.

In imaging terms: the pattern on the ground is the **object (the Sun) convolved with the point spread function (the aperture)**. **When the aperture is small compared to the Sun's projected size, the Sun's shape dominates.** On an ordinary day the Sun is a disk, so every spot is a round blob and nobody notices. During a partial eclipse the object turns into a crescent, and suddenly every spot is a crescent too.

## Solar eclipse as a PSF lab

:::{margin}
PSF = point spread function. Not the Python Software Foundation.
:::

A colander is a whole imaging lab you can hold in one hand. Typically we observe the colander image while standing, this puts the distance from colander to ground at about 4-5 feet. The image is dominated by the shape of the sun. What happens when the colander gets closer, almost touching the ground?

:::{figure} images/colander_distance_top60.mp4
:label: fig-colander-distance
:alt: Video of a colander's shadow on a white card during a partial eclipse. As the colander moves closer to the card, the spots of light change from small crescents to a blend to round dots the shape of the colander's holes.
:width: 100%

October 14, 2023: bringing the colander down toward the card. Far away, every spot is a crescent: the Sun. Up close, every spot is a round dot: the hole. In between, you see both.
:::

- **Colander close to the ground:** each spot is the shape of the **hole**, a little circle. That's just a shadow.
- **Colander far from the ground:** each spot is the shape of the **Sun**, a crescent.
- **In between:** you see both at once, the hole and the Sun blurred together. That's a convolution, live on the sidewalk.

Here's the math. Each spot on the ground is the hole's shape convolved with an image of the Sun:

$$
\text{spot}(x) = \text{Sun}_d(x) \circledast \text{hole}(x)
$$

Light from any single point on the Sun arrives as parallel rays, so each hole passes a beam the size of the hole, $a$. But the Sun isn't a point: light from its opposite edges arrives about $\theta \approx 0.53^\circ \approx 1/107$ radian apart, so the beams fan out and every spot grows with distance $d$:

$$
\text{Sun image width} \approx \theta d, \qquad \text{spot width} \approx a + \theta d
$$

So the spot is never exactly the size of the hole. Even 5 cm above the card, a 4 mm hole's spot is about 10% bigger: a slightly magnified, slightly blurred image of the hole. As $d$ grows, the $\theta d$ term takes over and the spot becomes an image of the Sun. The two terms are equal at the crossover distance

$$
d^* = \frac{a}{\theta} \approx 107\,a
$$

My colander's holes are about 4 mm across, so $d^* \approx 43$ cm. Within about 15 cm of the card you see the holes; around 40 cm, a blend; beyond a meter or so, the Sun. Below $d^*$, the hole dominates; above it, the Sun does. (Diffraction is negligible here: for a 4 mm hole at 1 m it blurs things by only about 0.1 mm.)

## Let's get the kids outside

In 2017 the eclipse came barely a week after school started. Our activity was organized on the fly, and I understand many students never went outside at all. What a tragedy.

Boulder's next good one is **Sunday, January 14, 2029**: 64% of the Sun covered, 8:25 to 11:22 AM, peaking at 9:50. It's on a weekend, so schools won't be organizing anything. That's fine. **No permission slip required.**

- **Host a colander party.** A front yard, a park, a cul-de-sac. Text the neighbors. Set out a few colanders, some index cards, and a box of eclipse glasses.
- **Partner with places that already do Sunday mornings:** libraries, the planetarium, scout troops, museums, congregations.
- **Make your own time-lapse.** Every 10 minutes, have the kids draw what they see. Line up the drawings afterward.
- **Share what you see.** Imagine crescent-covered sidewalks all over town on the same Sunday morning.

And mark your calendar for the next school-day partial: **Wednesday, March 30, 2033**, about 24% coverage, peaking around 11:49 AM, just before lunch. That's plenty of time to plan, so let's not improvise again.

### Try it yourself

- **Find a leafy tree** and look at the ground, or hold up a white card. This is the zero-effort version, and it's the most beautiful.
- **Use a colander, a saltine cracker, or a straw hat.** Instant pinhole arrays.
- **Cross your fingers in a waffle grid** and look at the shadow on the sidewalk.
- **Poke holes of different sizes** in a piece of cardboard and compare. Smaller holes give sharper but dimmer crescents. That's the resolution-versus-signal tradeoff every camera designer lives with.
- **Change the distance** between the holes and the card. The crescents grow with distance; the hole stays the same size.

:::{figure} images/kid_eclipse_glasses_2017.jpg
:label: fig-glasses
:alt: A young child sitting in the grass wearing paper eclipse glasses, looking up at the Sun

Total cost: one pair of paper eclipse glasses and a patch of lawn.
:::

**Safety:** never look directly at the Sun during a partial eclipse, even when it's mostly covered. Use eclipse glasses that meet the ISO 12312-2 standard, or just watch the projections. That's the point of this whole post anyway.

Partial eclipses are the perfect low-budget science lesson, for everyone. Get outside and do nerdy stuff.

## Extra Credit

*Due: any sunny day. No eclipse required.*

You don't have to wait until 2029 to see object ⊛ PSF in action. Swap the roles: keep the ordinary round Sun, and make the *holes* crescent-shaped.

1. Cut a few crescent-shaped holes, about 5 mm across, in a piece of cardboard.
2. Hold it in the sunshine just above the sidewalk. The spots of light are crescents: the shape of the hole.
3. Slowly raise it. Somewhere around half a meter, the crescents start to round off. By a meter or two, they're disks: the shape of the Sun.

That's the eclipse experiment run backwards. During an eclipse the Sun is the crescent, so crescents show up *far* from the holes. On an ordinary day the hole is the crescent, so crescents show up only *close*. Either way, far from the holes, you're looking at the Sun.

**Bonus problem:** the shapes switch over at about 100 times the hole size. Why 100?

:::{dropdown} Answer
The Sun is about half a degree across, roughly 1/107 of a radian. So at distance *d*, the Sun's image is about *d*/107 wide. When that's bigger than the hole, the Sun's shape wins.
:::

## Where will you be during the next eclipse?

Here's every eclipse worth stepping outside for in Boulder through 2048. Times are local.

| Date | Max coverage | Peak (local time) | Duration |
|---|---|---|---|
| **Sun, Jan 14, 2029** | **64%** | **9:50 AM** | **2 h 57 min** |
| Wed, Mar 30, 2033 | 24% | 11:49 AM | 1 h 57 min |
| Tue, Jun 21, 2039 | 14% | 10:03 AM | 2 h 00 min |
| Sun, Nov 4, 2040 | 23% | 11:39 AM | 2 h 10 min |
| Mon, Aug 22, 2044 | 77% | 7:46 PM | 43 min, cut short by sunset |
| Sat, Aug 12, 2045 | 99% | 10:38 AM | 2 h 26 min |
| Mon, Feb 5, 2046 | 35% | 5:24 PM | 37 min, cut short by sunset |
| Thu, Jun 11, 2048 | 85% | 5:32 AM (sunrise) | 59 min, already underway at sunrise |

Two more barely nick the Sun (5% at sunrise on Jan 26, 2028, and under 1% on Nov 14, 2031), so I've left them off.

August 12, 2045 is the big one: 99% in Boulder, and Colorado Springs gets over five minutes of totality.

**Not in Boulder?** Look up your next partial on [timeanddate.com's eclipse pages](https://www.timeanddate.com/eclipse/), which list every eclipse visible from your city, partials included. The free [Totality app](https://www.bigkidscience.com/?p=731) (made in Boulder by Big Kid Science, now run by the American Astronomical Society) shows what you'll see from your location during upcoming total eclipses.

---

### How I got these numbers

**Eclipse coverage.** "I" computed the eclipse geometry for every new moon between November 2026 and November 2031 using [Skyfield](https://rhodesmill.org/skyfield/) and NASA JPL's DE421 ephemeris. For each of about 34,000 cities with more than 15,000 people ([GeoNames](https://www.geonames.org/)), "I" found the largest fraction of the Sun's disk covered while the Sun was above the horizon. To estimate population, I scaled each city up to its country's total, which assumes rural people are spread out like the cities around them. The Boulder tables use the same geometry at one location, minute by minute.

**Eclipse by eclipse.** Out of every 1,000 people on Earth:

| Eclipse | Where | See at least half the Sun covered | In the path of totality |
|---|---|---|---|
| Feb 6, 2027 (annular) | South America, Africa | ~70 | none |
| Aug 2, 2027 (total) | Spain, North Africa, Middle East | ~110 | ~11 |
| Jan 26, 2028 (annular) | South America, Iberia | ~45 | none |
| Jul 22, 2028 (total) | Australia, New Zealand | ~40 | fewer than 1 |
| Jan 14, 2029 (partial) | North America | ~25 | none |
| Jun 1, 2030 (annular) | N. Africa, Europe, Asia | ~200 | none |
| Nov 25, 2030 (total) | Southern Africa, Australia | ~25 | about 1 |
| May 21, 2031 (annular) | Africa, South & Southeast Asia | ~205 | none |
| **At least once in five years** | | **~600 (6 in 10)** | **~13 (about 1 in 80)** |

**Checking it.** This approach reproduces published totality counts reasonably well: 6.8M vs. 6.3M for July 2028 and 9.1M vs. 10.6M for November 2030. It undercounts the August 2027 path (69M vs. ~89M), so the totality column uses the published figures from [timeanddate.com](https://www.timeanddate.com/eclipse/solar/2030-november-25) instead. Treat everything as good to roughly ±20%: these are residents only, from ~2020 population data, and weather isn't included.

**Flying.** In 2018, the most recent year with a careful global estimate, only about 1 in 9 people on Earth took a flight at all, and about 1 in 25 flew internationally. Even in the United States, more than half of people didn't fly that year. These figures come from Gössling & Humpe, "The global scale, distribution and growth of aviation: Implications for climate change," *Global Environmental Change* (2020), summarized [here](https://earth.org/frequent-flyers-aviation-carbon-emissions/). You'll often see the claim that "80% of people have never flown." According to [Our World in Data](https://ourworldindata.org/carbon-footprint-flying), there's no reliable global figure for that, and the number seems to trace back to a quote from a Boeing CEO, so I've left it out.

**Code.** The scripts are [`eclipse_pop.py`](code/eclipse_pop.py) (population counts), [`boulder_eclipses.py`](code/boulder_eclipses.py) (the Boulder tables), and [`make_timelapse.py`](code/make_timelapse.py) (the drawings animation).

## Thanks

Thank you to the Boulder SCIPYers for helping me push through my writer's block. This is my first time publishing with MyST and my first talk in over a decade, and I wouldn't have gotten here without the gentle push this event provided.

I would love feedback! Leave a comment or suggestion on [GitHub](https://github.com/tkeim/eclipse-post/issues).
