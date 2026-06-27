import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GOLD_DIR = PROJECT_ROOT / "data" / "gold"


def test_kpis_have_expected_business_fields():
    with (GOLD_DIR / "kpis.json").open(encoding="utf-8") as file:
        kpis = json.load(file)

    assert kpis["total_revenue"] > 0
    assert kpis["order_count"] > 0
    assert kpis["average_order_value"] > 0
    assert kpis["top_country"]
    assert kpis["top_category"]


def test_data_quality_report_tracks_governance_controls():
    with (GOLD_DIR / "data_quality_report.json").open(encoding="utf-8") as file:
        report = json.load(file)

    assert report["row_counts"]["raw_sales_rows"] >= report["row_counts"]["silver_sales_rows"]
    assert "duplicate_sales_removed" in report["quality_controls"]
    assert report["quality_score"]["customer_match_percent"] >= 0
    assert report["rgpd_minimization"]["gold_exposes_direct_identifiers"] is False


def test_lineage_links_kpis_to_source_layers():
    with (GOLD_DIR / "lineage.json").open(encoding="utf-8") as file:
        lineage = json.load(file)

    assert "kpis.json" in lineage
    assert "data/gold/enriched_sales.parquet" in lineage["kpis.json"]
    assert "data/raw/g_fact_sales.csv" in lineage["kpis.json"]
