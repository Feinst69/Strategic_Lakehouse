# Diagramme de flux d'ingestion Bronze / Silver / Gold

```mermaid
flowchart LR
    subgraph Sources["Sources silotees"]
        ERP["ERP on-premise<br/>g_fact_sales<br/>g_dim_products"]
        CRM["CRM SaaS<br/>g_dim_customers"]
        Exports["Exports analytiques<br/>CSV / Parquet"]
    end

    subgraph Bronze["Couche Bronze - donnees brutes"]
        BSales["sales.parquet"]
        BProducts["products.parquet"]
        BCustomers["customers.parquet"]
    end

    subgraph Silver["Couche Silver - donnees fiabilisees"]
        SSales["sales.parquet<br/>dates typees<br/>doublons supprimes"]
        SProducts["products.parquet<br/>cout type<br/>produits dedoublonnes"]
        SCustomers["customers.parquet<br/>dates typees<br/>clients dedoublonnes"]
    end

    subgraph Gold["Couche Gold - donnees BI"]
        Enriched["enriched_sales.parquet<br/>ventes + produits + clients"]
        KPIs["kpis.json<br/>CA total<br/>commandes<br/>panier moyen"]
        Aggs["revenue_by_*.csv<br/>pays<br/>categorie<br/>mois"]
        Quality["data_quality_report.json<br/>doublons<br/>completude<br/>RGPD"]
        Lineage["lineage.json<br/>provenance des KPI"]
    end

    subgraph Exposure["Exposition"]
        API["FastAPI<br/>/api/kpis"]
        QualityAPI["FastAPI<br/>/api/data-quality<br/>/api/lineage"]
        Dashboard["Dashboard HTML accessible"]
    end

    ERP --> BSales
    ERP --> BProducts
    CRM --> BCustomers
    Exports --> BSales

    BSales --> SSales
    BProducts --> SProducts
    BCustomers --> SCustomers

    SSales --> Enriched
    SProducts --> Enriched
    SCustomers --> Enriched

    Enriched --> KPIs
    Enriched --> Aggs
    Enriched --> Quality
    Enriched --> Lineage
    KPIs --> API
    Quality --> QualityAPI
    Lineage --> QualityAPI
    API --> Dashboard
    QualityAPI --> Dashboard
```

## A defendre

Le flux illustre la valeur ajoutee de chaque couche. Bronze securise l'ingestion, Silver rend les donnees fiables, Gold produit des indicateurs et des controles de gouvernance, puis l'API permet de les consommer sans acceder directement aux fichiers internes.
