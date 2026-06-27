from pathlib import Path

import pandas as pd


def build_gold(silver_dir: Path, gold_dir: Path) -> dict[str, Path]:
    """Create BI-ready KPI tables from Silver tables."""
    gold_dir.mkdir(parents=True, exist_ok=True)

    sales = pd.read_parquet(silver_dir / "sales.parquet")
    products = pd.read_parquet(silver_dir / "products.parquet")
    customers = pd.read_parquet(silver_dir / "customers.parquet")

    enriched_sales = (
        sales.merge(products[["product_key", "product_name", "category", "sub_category"]], on="product_key", how="left")
        .merge(customers[["customer_key", "country", "gender"]], on="customer_key", how="left")
    )
    enriched_sales["year"] = enriched_sales["order_date"].dt.year
    enriched_sales["month"] = enriched_sales["order_date"].dt.to_period("M").astype(str)

    kpis = {
        "total_revenue": float(enriched_sales["sales"].sum()),
        "order_count": int(enriched_sales["order_number"].nunique()),
        "quantity_sold": int(enriched_sales["quantity"].sum()),
        "average_order_value": float(enriched_sales.groupby("order_number")["sales"].sum().mean()),
        "top_country": str(enriched_sales.groupby("country")["sales"].sum().idxmax()),
        "top_category": str(enriched_sales.groupby("category")["sales"].sum().idxmax()),
    }

    revenue_by_country = (
        enriched_sales.groupby("country", dropna=False)["sales"]
        .sum()
        .reset_index()
        .rename(columns={"sales": "revenue"})
        .sort_values("revenue", ascending=False)
    )
    revenue_by_category = (
        enriched_sales.groupby("category", dropna=False)["sales"]
        .sum()
        .reset_index()
        .rename(columns={"sales": "revenue"})
        .sort_values("revenue", ascending=False)
    )
    revenue_by_month = (
        enriched_sales.groupby("month", dropna=False)["sales"]
        .sum()
        .reset_index()
        .rename(columns={"sales": "revenue"})
        .sort_values("month")
    )

    outputs = {
        "enriched_sales": gold_dir / "enriched_sales.parquet",
        "kpis": gold_dir / "kpis.json",
        "revenue_by_country": gold_dir / "revenue_by_country.csv",
        "revenue_by_category": gold_dir / "revenue_by_category.csv",
        "revenue_by_month": gold_dir / "revenue_by_month.csv",
    }

    enriched_sales.to_parquet(outputs["enriched_sales"], index=False)
    pd.Series(kpis).to_json(outputs["kpis"], indent=2)
    revenue_by_country.to_csv(outputs["revenue_by_country"], index=False)
    revenue_by_category.to_csv(outputs["revenue_by_category"], index=False)
    revenue_by_month.to_csv(outputs["revenue_by_month"], index=False)

    return outputs
