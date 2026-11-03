# Ocular Macular Pigment Optical Density (MPOD) Personal Agent Skill

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)]()
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20JSON--RPC-orange.svg)]()
[![Production Ready](https://img.shields.io/badge/status-production--ready-green.svg)]()

Deterministic, zero-mock personal agent micro-skill for calculating Foveal Center Macular Pigment Optical Density (MPOD in du), Spatial Profile Decay, Macular Pigment Volume (MPV), and AMD photoprotection level using heterochromatic flicker photometry principles.

## Architecture

```mermaid
flowchart TD
    A[HFP 460 nm Blue vs 540 nm Green Reference] --> B[Compute Peak Foveal MPOD du]
    B --> C[Model Exponential Spatial Decline MPOD r]
    C --> D[Compute 460 nm Blue Light Absorption %]
    D --> E[Integrate Macular Pigment Volume MPV]
    E --> F[Stratify AMD Phototoxic Vulnerability]
```

## Quickstart

```python
from client import MacularPigmentOpticalDensityClient

client = MacularPigmentOpticalDensityClient()
result = client.evaluate_mpod(
    foveal_peak_mpod_du=0.62,
    profile_decay_constant=0.85
)
print(result)
```

## License

Apache-2.0
