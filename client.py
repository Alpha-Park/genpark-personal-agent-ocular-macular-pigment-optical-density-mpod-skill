"""
Ocular Macular Pigment Optical Density (MPOD) & Carotenoid Kinetics Client.
Zero-mock pure Python standard library implementation.
Calculates Foveal Center MPOD, Spatial Profile Decay, Macular Pigment Volume (MPV),
and AMD phototoxic vulnerability index based on heterochromatic flicker photometry principles.
"""

import math
from typing import Dict, Any, List, Optional


class MacularPigmentOpticalDensityClient:
    """
    Evaluates foveal lutein, zeaxanthin, and meso-zeaxanthin carotenoid density:
    - Foveal peak MPOD (optical density units, du: 0.0 to 1.0)
    - Eccentricity spatial profile decline: MPOD(r) = MPOD_0 * exp(-decay_rate * r)
    - Macular Pigment Volume (MPV): spatial integration over central 6 degrees
    - Photostress Recovery & Blue Light filtration efficiency
    """

    def __init__(self):
        pass

    def evaluate_mpod(
        self,
        foveal_peak_mpod_du: float,
        profile_decay_constant: Optional[float] = 0.85,
        eccentricity_samples_deg: Optional[List[float]] = None,
        patient_age_years: Optional[int] = 45,
        eye_examined: Optional[str] = "OD"
    ) -> Dict[str, Any]:
        """
        Calculates MPOD profile and blue-light shielding parameters.
        foveal_peak_mpod_du: central peak MPOD in density units (0.05 to 1.0 du).
        profile_decay_constant: spatial decline coefficient k (typically 0.6 to 1.2 per degree).
        eccentricity_samples_deg: list of eccentricities to evaluate (default: [0.0, 0.5, 1.0, 2.0, 4.0]).
        """
        if foveal_peak_mpod_du <= 0 or foveal_peak_mpod_du > 1.2:
            raise ValueError("Foveal peak MPOD must be between 0.01 and 1.2 optical density units.")
        if profile_decay_constant <= 0:
            raise ValueError("Profile decay constant must be strictly positive.")

        if eccentricity_samples_deg is None:
            eccentricity_samples_deg = [0.0, 0.5, 1.0, 2.0, 4.0]

        # Calculate spatial distribution
        spatial_profile = []
        for r in eccentricity_samples_deg:
            val = foveal_peak_mpod_du * math.exp(-profile_decay_constant * r)
            spatial_profile.append({
                "eccentricity_deg": round(r, 2),
                "mpod_du": round(val, 3)
            })

        # Blue light (460 nm) transmittance at foveal center:
        # Transmittance T = 10^(-MPOD)
        # Blue light absorption = (1 - T) * 100%
        blue_transmittance = 10.0 ** (-foveal_peak_mpod_du)
        blue_absorption_pct = (1.0 - blue_transmittance) * 100.0

        # Macular Pigment Volume (MPV) approximation over 0 to 4 degrees:
        # Volume = 2 * pi * integral(r * MPOD(r) dr)
        # Analytical integral of r * exp(-k*r) = (1/k^2) * [1 - (k*R + 1)*exp(-k*R)]
        k = profile_decay_constant
        r_max = 4.0
        integral_term = (1.0 / (k * k)) * (1.0 - (k * r_max + 1.0) * math.exp(-k * r_max))
        mpv_approx = 2.0 * math.pi * foveal_peak_mpod_du * integral_term

        # Clinical AMD risk and carotenoid classification:
        # MPOD >= 0.45 du: Robust Macular Carotenoid Shield (optimal protection, low AMD phototoxicity)
        # MPOD 0.25 - 0.44 du: Moderate / Borderline Carotenoid Density
        # MPOD < 0.25 du: Depleted Macular Pigment / High Phototoxic Vulnerability
        if foveal_peak_mpod_du >= 0.45:
            carotenoid_status = "Optimal / Robust Macular Carotenoid Density"
            photoprotection_level = "High; superior foveal filtration of 460 nm phototoxic high-energy visible (HEV) blue light and accelerated photostress recovery."
        elif foveal_peak_mpod_du >= 0.25:
            carotenoid_status = "Moderate / Sub-optimal Macular Pigment"
            photoprotection_level = "Moderate; intermediate blue light attenuation, dietary xanthophyll supplementation (lutein/zeaxanthin) recommended."
        else:
            carotenoid_status = "Depleted Macular Pigment / High Vulnerability"
            photoprotection_level = "Low; substantial foveal oxidative risk and elevated epidemiological susceptibility to age-related macular degeneration (AMD)."

        return {
            "status": "success",
            "foveal_metrics": {
                "peak_mpod_du": round(foveal_peak_mpod_du, 3),
                "blue_light_460nm_absorption_pct": round(blue_absorption_pct, 1),
                "blue_light_460nm_transmittance_pct": round(blue_transmittance * 100.0, 1),
                "macular_pigment_volume_mpv": round(mpv_approx, 2)
            },
            "spatial_distribution": spatial_profile,
            "clinical_assessment": {
                "carotenoid_status": carotenoid_status,
                "photoprotection_level": photoprotection_level,
                "eye_examined": eye_examined
            }
        }
