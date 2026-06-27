import json
from pathlib import Path

import pandas as pd


def _read_csv(source: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(source)
    except UnicodeDecodeError:
        return pd.read_csv(source, encoding="latin1")


def _percent(part: int | float, total: int | float) -> float:
    if total == 0:
        return 0.0
    return round((part / total) * 100, 2)


def build_data_quality_report(raw_dir: Path, silver_dir: Path, gold_dir: Path) -> dict[str, Path]:
    """Create governance-oriented data quality and lineage outputs."""
    gold_dir.mkdir(parents=True, exist_ok=True)

    raw_sales = _read_csv(raw_dir / "g_fact_sales.csv")
    raw_products = _read_csv(raw_dir / "g_dim_products.csv")
    raw_customers = _read_csv(raw_dir / "g_dim_customers.csv")

    silver_sales = pd.read_parquet(silver_dir / "sales.parquet")
    silver_products = pd.read_parquet(silver_dir / "products.parquet")
    silver_customers = pd.read_parquet(silver_dir / "customers.parquet")
    enriched_sales = pd.read_parquet(gold_dir / "enriched_sales.parquet")

    raw_sales_duplicates = int(raw_sales.duplicated(subset=["order_number", "customer_key", "product_key"]).sum())
    raw_product_duplicates = int(raw_products.duplicated(subset=["product_key"]).sum())
    raw_customer_duplicates = int(raw_customers.duplicated(subset=["customer_key"]).sum())
    missing_customer_matches = int(enriched_sales["country"].isna().sum())
    missing_product_matches = int(enriched_sales["category"].isna().sum())
    invalid_sales_dates = int(pd.to_datetime(raw_sales["order_date"], errors="coerce").isna().sum())

    report = {
        "row_counts": {
            "raw_sales_rows": int(len(raw_sales)),
            "silver_sales_rows": int(len(silver_sales)),
            "raw_products_rows": int(len(raw_products)),
            "silver_products_rows": int(len(silver_products)),
            "raw_customers_rows": int(len(raw_customers)),
            "silver_customers_rows": int(len(silver_customers)),
            "gold_enriched_sales_rows": int(len(enriched_sales)),
        },
        "quality_controls": {
            "duplicate_sales_removed": raw_sales_duplicates,
            "duplicate_products_removed": raw_product_duplicates,
            "duplicate_customers_removed": raw_customer_duplicates,
            "invalid_order_dates": invalid_sales_dates,
            "missing_customer_matches": missing_customer_matches,
            "missing_product_matches": missing_product_matches,
        },
        "quality_score": {
            "sales_row_retention_percent": _percent(len(silver_sales), len(raw_sales)),
            "customer_match_percent": round(100 - _percent(missing_customer_matches, len(enriched_sales)), 2),
            "product_match_percent": round(100 - _percent(missing_product_matches, len(enriched_sales)), 2),
        },
        "rgpd_minimization": {
            "gold_exposes_direct_identifiers": False,
            "excluded_personal_fields": ["first_name", "last_name", "birth_date", "customer_number"],
            "exposed_customer_fields": ["customer_key", "country", "gender"],
        },
    }

    lineage = {
        "kpis.json": [
            "data/gold/enriched_sales.parquet",
            "data/silver/sales.parquet",
            "data/silver/products.parquet",
            "data/silver/customers.parquet",
            "data/raw/g_fact_sales.csv",
            "data/raw/g_dim_products.csv",
            "data/raw/g_dim_customers.csv",
        ],
        "revenue_by_country.csv": ["data/gold/enriched_sales.parquet"],
        "revenue_by_category.csv": ["data/gold/enriched_sales.parquet"],
        "revenue_by_month.csv": ["data/gold/enriched_sales.parquet"],
    }

    outputs = {
        "data_quality_report": gold_dir / "data_quality_report.json",
        "lineage": gold_dir / "lineage.json",
    }
    outputs["data_quality_report"].write_text(json.dumps(report, indent=2), encoding="utf-8")
    outputs["lineage"].write_text(json.dumps(lineage, indent=2), encoding="utf-8")

    return outputs
