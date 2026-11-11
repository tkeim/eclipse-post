# Saved for later: the PSF lab math

Cut from the "Solar eclipse as a PSF lab" section of `index.md`. To revive it, paste it back
after the "In imaging terms" paragraph. This file is excluded from the site build.

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
