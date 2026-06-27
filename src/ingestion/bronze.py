from pathlib import Path

import pandas as pd


RAW_FILES = {
    "sales": "g_fact_sales.csv",
    "products": "g_dim_products.csv",
    "customers": "g_dim_customers.csv",
}


def ingest_raw_to_bronze(raw_dir: Path, bronze_dir: Path) -> dict[str, Path]:
    """Copy raw business CSV files into Bronze as queryable parquet files."""
    bronze_dir.mkdir(parents=True, exist_ok=True)
    written_files: dict[str, Path] = {}

    for domain, filename in RAW_FILES.items():
        source = raw_dir / filename
        target = bronze_dir / f"{domain}.parquet"
        try:
            dataframe = pd.read_csv(source)
        except UnicodeDecodeError:
            dataframe = pd.read_csv(source, encoding="latin1")
        dataframe.to_parquet(target, index=False)
        written_files[domain] = target

    return written_files
