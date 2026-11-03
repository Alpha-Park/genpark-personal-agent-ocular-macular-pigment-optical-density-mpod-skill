---
name: genpark-personal-agent-ocular-macular-pigment-optical-density-mpod-skill
version: 1.0.0
description: Calculates Foveal Center Macular Pigment Optical Density (MPOD in du), Spatial Profile Decay, Macular Pigment Volume (MPV), and AMD photoprotection level.
authors:
  - GenPark Ecosystem
tags:
  - personal-agent
  - ophthalmology
  - mpod
  - macular-pigment
  - lutein
  - amd
  - zero-dependency
---

# Ocular Macular Pigment Optical Density (MPOD) Skill

## Mathematical Formulation

Spatial decay profile from foveal center ($r$ in visual degrees):

$$\text{MPOD}(r) = \text{MPOD}_0 \times \exp(-k \times r)$$

Blue light ($460\text{ nm}$) transmittance and absorption:

$$T_{460} = 10^{-\text{MPOD}_0}$$
$$\text{Absorption}_{460} \, (\%) = (1 - T_{460}) \times 100$$

Macular Pigment Volume (MPV, central $4^\circ$ integration):

$$\text{MPV} = 2\pi \, \text{MPOD}_0 \int_0^{R} r e^{-k r} \, dr = 2\pi \, \text{MPOD}_0 \left[\frac{1}{k^2} \left(1 - (k R + 1) e^{-k R}\right)\right]$$

## Clinical Photoprotection Stratification
- **Optimal / Robust Protection**: $\text{MPOD}_0 \ge 0.45\text{ du}$ ($> 65\%$ blue filtration, fast glare recovery)
- **Moderate / Sub-optimal Protection**: $\text{MPOD}_0 \in [0.25, 0.44]\text{ du}$
- **Depleted Pigment / High AMD Vulnerability**: $\text{MPOD}_0 < 0.25\text{ du}$ ($< 44\%$ blue filtration, increased retinal photo-oxidative stress)
