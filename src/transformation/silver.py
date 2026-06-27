from pathlib import Path

import pandas as pd


def _clean_text_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe = dataframe.copy()
    for column in dataframe.select_dtypes(include="object").columns:
        dataframe[column] = dataframe[column].astype(str).str.strip()
    return dataframe


def build_silver(bronze_dir: Path, silver_dir: Path) -> dict[str, Path]:
    """Clean, type and deduplicate Bronze tables into Silver tables."""
    silver_dir.mkdir(parents=True, exist_ok=True)

    sales = pd.read_parquet(bronze_dir / "sales.parquet")
    products = pd.read_parquet(bronze_dir / "products.parquet")
    customers = pd.read_parquet(bronze_dir / "customers.parquet")

    sales = _clean_text_columns(sales)
    products = _clean_text_columns(products)
    customers = _clean_text_columns(customers)

    sales["order_date"] = pd.to_datetime(sales["order_date"], errors="coerce")
    sales["shipping_date"] = pd.to_datetime(sales["shipping_date"], errors="coerce")
    sales["due_date"] = pd.to_datetime(sales["due_date"], errors="coerce")
    sales["sales"] = pd.to_numeric(sales["sales"], errors="coerce").fillna(0)
    sales["quantity"] = pd.to_numeric(sales["quantity"], errors="coerce").fillna(0).astype(int)
    sales["price"] = pd.to_numeric(sales["price"], errors="coerce").fillna(0)
    sales = sales.dropna(subset=["order_number", "customer_key", "product_key", "order_date"])
    sales = sales.drop_duplicates(subset=["order_number", "customer_key", "product_key"])

    products["cost"] = pd.to_numeric(products["cost"], errors="coerce").fillna(0)
    products["start_date"] = pd.to_datetime(products["start_date"], errors="coerce")
    products = products.drop_duplicates(subset=["product_key"])

    customers["birth_date"] = pd.to_datetime(customers["birth_date"], errors="coerce")
    customers["create_date"] = pd.to_datetime(customers["create_date"], errors="coerce")
    customers = customers.drop_duplicates(subset=["customer_key"])

    outputs = {
        "sales": silver_dir / "sales.parquet",
        "products": silver_dir / "products.parquet",
        "customers": silver_dir / "customers.parquet",
    }

    sales.to_parquet(outputs["sales"], index=False)
    products.to_parquet(outputs["products"], index=False)
    customers.to_parquet(outputs["customers"], index=False)

    return outputs
