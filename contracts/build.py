# Build the sample contract in this directory using Beaker and output to ./artifacts
from pathlib import Path

from contracts.nft_as_collateral import nft_as_collateral_app


def build() -> Path:
    app_spec = nft_as_collateral_app.build()
    output_dir = Path(__file__).parent / "artifacts"
    print(f"Dumping {app_spec.contract.name} to {output_dir}")
    app_spec.export(output_dir)
    return output_dir / "application.json"


if __name__ == "__main__":
    build()
