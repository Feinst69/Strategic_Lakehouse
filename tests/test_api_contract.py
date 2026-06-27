from src.api.main import get_data_quality, get_kpis, get_lineage


def test_kpi_api_contract():
    kpis = get_kpis()

    assert set(kpis) >= {
        "total_revenue",
        "order_count",
        "quantity_sold",
        "average_order_value",
        "top_country",
        "top_category",
    }


def test_data_quality_api_contract():
    report = get_data_quality()

    assert "row_counts" in report
    assert "quality_controls" in report
    assert "quality_score" in report
    assert "rgpd_minimization" in report


def test_lineage_api_contract():
    lineage = get_lineage()

    assert "kpis.json" in lineage
