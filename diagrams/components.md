# Diagramme de composants Lakehouse

```mermaid
C4Component
    title Composants internes du POC Strategic Lakehouse

    Container_Boundary(poc, "Strategic Lakehouse POC") {
        Component(raw_csv, "CSV sources", "Fichiers", "Donnees brutes issues des silos ERP, CRM et exports analytiques")
        Component(bronze_script, "Ingestion Bronze", "Python / Pandas", "Lit les CSV sources et les materialise en tables Bronze")
        Component(bronze_store, "Stockage Bronze", "Parquet", "Conserve les donnees proches du brut")
        Component(silver_script, "Transformation Silver", "Python / Pandas", "Nettoie, type et dedoublonne les donnees")
        Component(silver_store, "Stockage Silver", "Parquet", "Contient les donnees fiabilisees")
        Component(gold_script, "Construction Gold", "Python / Pandas", "Joint les domaines et calcule les KPI BI")
        Component(gold_store, "Stockage Gold", "JSON / CSV / Parquet", "Expose des jeux de donnees agreges et consommables")
        Component(governance, "Controles gouvernance", "Python / JSON", "Produit le rapport qualite, le lineage et les controles RGPD")
        Component(api, "API BI", "FastAPI", "Retourne les KPI Gold au format JSON")
        Component(web, "Dashboard accessible", "HTML / JS", "Affiche les KPI avec structure semantique et contraste lisible")
    }

    Rel(raw_csv, bronze_script, "Est ingere par")
    Rel(bronze_script, bronze_store, "Ecrit")
    Rel(bronze_store, silver_script, "Alimente")
    Rel(silver_script, silver_store, "Ecrit")
    Rel(silver_store, gold_script, "Alimente")
    Rel(gold_script, gold_store, "Ecrit")
    Rel(silver_store, governance, "Alimente")
    Rel(gold_store, governance, "Alimente")
    Rel(governance, gold_store, "Ecrit rapport qualite et lineage")
    Rel(gold_store, api, "Est lu par")
    Rel(api, web, "Expose", "HTTP JSON")
```

## A defendre

Chaque composant correspond a une responsabilite claire. Le POC reste simple, mais il respecte la logique d'une architecture Lakehouse : ingestion, stockage par couches, transformation progressive, controles de gouvernance, puis exposition BI via API.
