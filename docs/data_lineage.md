# Lineage des donnees

## Objectif

Le lineage documente l'origine des donnees et les transformations appliquees jusqu'aux livrables BI. Il repond a un enjeu de gouvernance : etre capable d'expliquer d'ou vient un KPI et quelles couches l'ont produit.

## Flux principal

```text
data/raw/g_fact_sales.csv
data/raw/g_dim_products.csv
data/raw/g_dim_customers.csv
        |
        v
data/bronze/sales.parquet
data/bronze/products.parquet
data/bronze/customers.parquet
        |
        v
data/silver/sales.parquet
data/silver/products.parquet
data/silver/customers.parquet
        |
        v
data/gold/enriched_sales.parquet
        |
        v
data/gold/kpis.json
data/gold/revenue_by_country.csv
data/gold/revenue_by_category.csv
data/gold/revenue_by_month.csv
```

## Lineage machine-readable

Le pipeline genere aussi :

```text
data/gold/lineage.json
```

Ce fichier peut etre consomme par un outil de gouvernance, un catalogue de donnees ou un futur agent IA interne.

## A defendre

Le lineage rend la BI auditable. Si le COMEX demande d'ou vient le chiffre d'affaires total, on peut remonter du KPI Gold jusqu'aux fichiers sources.
