from pathlib import Path

from src.ingestion.bronze import ingest_raw_to_bronze
from src.transformation.gold import build_gold
from src.transformation.silver import build_silver


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def run_pipeline() -> None:
    raw_dir = DATA_DIR / "raw"
    bronze_dir = DATA_DIR / "bronze"
    silver_dir = DATA_DIR / "silver"
    gold_dir = DATA_DIR / "gold"

    print("Bronze: ingestion des CSV bruts")
    bronze_outputs = ingest_raw_to_bronze(raw_dir, bronze_dir)
    for name, path in bronze_outputs.items():
        print(f"  - {name}: {path.relative_to(PROJECT_ROOT)}")

    print("Silver: nettoyage, typage, dedoublonnage")
    silver_outputs = build_silver(bronze_dir, silver_dir)
    for name, path in silver_outputs.items():
        print(f"  - {name}: {path.relative_to(PROJECT_ROOT)}")

    print("Gold: calcul des KPI BI")
    gold_outputs = build_gold(silver_dir, gold_dir)
    for name, path in gold_outputs.items():
        print(f"  - {name}: {path.relative_to(PROJECT_ROOT)}")

    print("Pipeline termine.")


if __name__ == "__main__":
    run_pipeline()
