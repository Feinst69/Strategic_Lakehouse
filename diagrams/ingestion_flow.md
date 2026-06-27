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
    end

    subgraph Exposure["Exposition"]
        API["FastAPI<br/>/api/kpis"]
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
    KPIs --> API
    API --> Dashboard
```

## A defendre

Le flux illustre la valeur ajoutee de chaque couche. Bronze securise l'ingestion, Silver rend les donnees fiables, Gold produit des indicateurs directement exploitables par la BI, puis l'API permet de consommer ces indicateurs sans acceder directement aux fichiers internes.
