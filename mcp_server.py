"""
MCP Server for Ocular Macular Pigment Optical Density (MPOD) Skill.
Provides standard Model Context Protocol JSON-RPC tool endpoints.
"""

import sys
import json
from client import MacularPigmentOpticalDensityClient


def main():
    client = MacularPigmentOpticalDensityClient()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue

        method = req.get("method")
        msg_id = req.get("id")

        if method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "tools": [
                        {
                            "name": "evaluate_mpod",
                            "description": "Calculates Foveal Center Macular Pigment Optical Density (MPOD in du), Spatial Profile Decay, Macular Pigment Volume (MPV), and AMD photoprotection level.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "foveal_peak_mpod_du": {
                                        "type": "number",
                                        "description": "Foveal peak MPOD in optical density units (du, e.g. 0.05 to 1.0)."
                                    },
                                    "profile_decay_constant": {
                                        "type": "number",
                                        "description": "Spatial profile decay constant k per degree (default: 0.85)."
                                    },
                                    "eccentricity_samples_deg": {
                                        "type": "array",
                                        "items": {"type": "number"},
                                        "description": "Retinal eccentricity sample points in visual degrees."
                                    },
                                    "patient_age_years": {
                                        "type": "integer",
                                        "description": "Subject age in years (optional)."
                                    },
                                    "eye_examined": {
                                        "type": "string",
                                        "description": "OD (right) or OS (left)."
                                    }
                                },
                                "required": [
                                    "foveal_peak_mpod_du"
                                ]
                            }
                        }
                    ]
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})

            if name == "evaluate_mpod":
                try:
                    out = client.evaluate_mpod(**args)
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps(out, indent=2)}]
                        }
                    }
                except Exception as e:
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "isError": True,
                        "error": {"code": -32000, "message": str(e)}
                    }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    main()
