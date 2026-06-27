# Diagramme de contexte systeme

```mermaid
C4Context
    title Contexte SI cible - GlobalTrade Solutions

    Person(comex, "COMEX / Direction", "Consulte les indicateurs strategiques")
    Person(data_analyst, "Data analyst", "Analyse les ventes, les clients et les stocks")
    Person(bi_user, "Collaborateur metier", "Consomme les KPI depuis un dashboard accessible")

    System_Boundary(globaltrade, "GlobalTrade Solutions") {
        System(erp, "GlobalTrade ERP", "ERP on-premise contenant produits, stocks et ventes historiques")
        System(crm, "GlobalTrade CRM Cloud", "CRM SaaS contenant clients et interactions commerciales")
        System(files, "Fichiers analytiques", "Exports CSV/Parquet issus de traitements locaux")
        System(lakehouse, "Strategic Lakehouse", "Plateforme unifiee Bronze/Silver/Gold exposant des KPI BI")
        System(dashboard, "Dashboard BI accessible", "Interface web consommant les KPI Gold via API")
    }

    Rel(erp, lakehouse, "Alimente", "CSV / batch")
    Rel(crm, lakehouse, "Alimente", "CSV / API future")
    Rel(files, lakehouse, "Alimente", "CSV / Parquet")
    Rel(lakehouse, dashboard, "Expose les KPI", "API JSON")
    Rel(comex, dashboard, "Consulte")
    Rel(data_analyst, lakehouse, "Explore et controle les donnees")
    Rel(bi_user, dashboard, "Consulte")
```

## A defendre

Ce diagramme montre le passage d'un SI fragmente vers un systeme analytique unifie. L'ERP, le CRM et les fichiers restent des sources distinctes, mais le Lakehouse devient la couche centrale de consolidation, de qualite et d'exposition BI.
