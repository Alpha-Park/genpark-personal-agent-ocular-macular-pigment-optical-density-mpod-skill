"""
Example usage of Ocular Macular Pigment Optical Density (MPOD) Skill.
Demonstrates robust carotenoid photoprotection vs depleted MPOD AMD vulnerability.
"""

import json
from client import MacularPigmentOpticalDensityClient


def main():
    print("=== Testing Ocular MPOD Skill ===")
    client = MacularPigmentOpticalDensityClient()

    # 1. Healthy young adult with high carotenoid diet (Foveal peak MPOD = 0.62 du -> 76% blue absorption, optimal protection)
    res_robust = client.evaluate_mpod(
        foveal_peak_mpod_du=0.62,
        profile_decay_constant=0.85,
        patient_age_years=32,
        eye_examined="OD"
    )
    print("\n[Case 1: Robust Macular Carotenoid Density]")
    print(json.dumps(res_robust, indent=2))

    # 2. Elderly subject with depleted macular pigment (Foveal peak MPOD = 0.14 du -> 27% blue absorption, high AMD risk)
    res_depleted = client.evaluate_mpod(
        foveal_peak_mpod_du=0.14,
        profile_decay_constant=0.90,
        patient_age_years=74,
        eye_examined="OS"
    )
    print("\n[Case 2: Depleted Macular Pigment / AMD Phototoxicity Risk]")
    print(json.dumps(res_depleted, indent=2))

    # Assertions
    assert res_robust["foveal_metrics"]["blue_light_460nm_absorption_pct"] > 70.0
    assert "Optimal" in res_robust["clinical_assessment"]["carotenoid_status"]
    assert res_depleted["foveal_metrics"]["blue_light_460nm_absorption_pct"] < 35.0
    assert "Depleted" in res_depleted["clinical_assessment"]["carotenoid_status"]
    print("\n[SUCCESS] Ocular MPOD tests passed!")


if __name__ == "__main__":
    main()
