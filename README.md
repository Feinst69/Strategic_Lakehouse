# Strategic Lakehouse

POC minimal d'une architecture Lakehouse pour GlobalTrade Solutions.

Le prototype suit le parcours attendu en soutenance :

1. ingestion des CSV sources en couche Bronze ;
2. nettoyage, typage et dedoublonnage en couche Silver ;
3. calcul de KPI BI en couche Gold ;
4. exposition des KPI via une API FastAPI ;
5. affichage des KPI dans une interface web accessible ;
6. generation d'un rapport qualite et d'un lineage pour la gouvernance.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Si les dependances sont deja disponibles dans l'environnement, l'etape `pip install` peut etre ignoree.

## Lancer le pipeline Lakehouse

```bash
python -m src.pipeline
```

Cette commande produit :

- `data/bronze/*.parquet` : copie structurée des donnees brutes ;
- `data/silver/*.parquet` : donnees nettoyees et typees ;
- `data/gold/kpis.json` : KPI BI exposes par l'API ;
- `data/gold/revenue_by_*.csv` : agregats BI complementaires.
- `data/gold/data_quality_report.json` : controles qualite et minimisation RGPD ;
- `data/gold/lineage.json` : provenance des sorties Gold.

## Lancer l'API et le dashboard

```bash
uvicorn src.api.main:app --reload
```

Puis ouvrir :

- dashboard : `http://127.0.0.1:8000`
- API KPI : `http://127.0.0.1:8000/api/kpis`
- API qualite : `http://127.0.0.1:8000/api/data-quality`
- API lineage : `http://127.0.0.1:8000/api/lineage`
- documentation API : `http://127.0.0.1:8000/docs`

## KPI Gold exposes

- chiffre d'affaires total ;
- nombre de commandes ;
- quantite vendue ;
- panier moyen ;
- pays generant le plus de chiffre d'affaires ;
- categorie produit generant le plus de chiffre d'affaires.

## Bonus gouvernance

Le pipeline produit aussi un rapport qualite des donnees :

- nombre de lignes Raw, Silver et Gold ;
- doublons detectes ;
- dates invalides ;
- correspondance ventes / clients ;
- correspondance ventes / produits ;
- verification de minimisation RGPD sur les champs exposes en Gold.

Le fichier `lineage.json` permet de remonter des KPI Gold jusqu'aux sources CSV.

## Tests

Apres avoir lance le pipeline :

```bash
python -m pytest
```

Les tests verifient le contrat des KPI, la presence du rapport qualite et le lineage.

## Script de demo

```bash
bash scripts/demo.sh
```

## Accessibilite du dashboard

Le prototype integre les bases attendues pour une demonstration :

- structure HTML semantique avec `header`, `main`, `section`, titres hierarchises ;
- zone de statut avec `role="status"` et mise a jour lisible par lecteur d'ecran ;
- contraste fort entre texte et fond ;
- navigation clavier possible sur le bouton d'actualisation ;
- focus visible.
