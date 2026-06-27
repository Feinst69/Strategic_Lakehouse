# Specification technique

## Architecture de donnees Bronze / Silver / Gold

### Couche Bronze

La couche Bronze contient les donnees proches du brut. Elle sert de zone d'atterrissage et de tracabilite.

| Table | Source | Description |
|---|---|---|
| `bronze/sales.parquet` | `g_fact_sales.csv` | ventes historiques issues de l'ERP |
| `bronze/products.parquet` | `g_dim_products.csv` | referentiel produits |
| `bronze/customers.parquet` | `g_dim_customers.csv` | referentiel clients |

Justification : cette couche conserve une copie exploitable des donnees sources sans appliquer de logique metier forte.

### Couche Silver

La couche Silver contient des donnees nettoyees, typees et dedoublonnees.

| Table | Transformations |
|---|---|
| `silver/sales.parquet` | typage des dates, conversion des montants et quantites, suppression des lignes invalides, dedoublonnage |
| `silver/products.parquet` | nettoyage texte, typage du cout, dedoublonnage par `product_key` |
| `silver/customers.parquet` | nettoyage texte, typage des dates client, dedoublonnage par `customer_key` |

Justification : cette couche fournit une base fiable et reutilisable par plusieurs usages analytiques.

### Couche Gold

La couche Gold contient les donnees pretes pour la BI.

| Sortie | Description |
|---|---|
| `gold/enriched_sales.parquet` | ventes enrichies avec donnees produit et client |
| `gold/kpis.json` | KPI exposes par l'API |
| `gold/revenue_by_country.csv` | chiffre d'affaires par pays |
| `gold/revenue_by_category.csv` | chiffre d'affaires par categorie |
| `gold/revenue_by_month.csv` | chiffre d'affaires par mois |
| `gold/data_quality_report.json` | controles qualite, completude et minimisation RGPD |
| `gold/lineage.json` | provenance des sorties Gold |

Justification : cette couche evite aux consommateurs BI de refaire les jointures et les calculs. Elle fournit des donnees stables, comprehensibles et directement exploitables.

## Fonctionnalites priorisees

| Fonctionnalite | Description | Critere d'acceptation | Priorite |
|---|---|---|---|
| Ingestion CSV | Lire les fichiers sources depuis `data/raw` | les fichiers Bronze sont generes sans erreur | Must |
| Stockage Bronze | Materialiser les donnees brutes en Parquet | `data/bronze/*.parquet` existe apres pipeline | Must |
| Transformation Silver | Nettoyer, typer et dedoublonner les donnees | les dates et montants sont exploitables en calcul | Must |
| Construction Gold | Produire des KPI et agregats BI | `data/gold/kpis.json` contient les KPI attendus | Must |
| API BI | Exposer les KPI au format JSON | `/api/kpis` retourne HTTP 200 avec les indicateurs | Must |
| Dashboard web | Afficher les KPI dans une page HTML | les KPI sont visibles depuis `/` | Should |
| Accessibilite de base | Respecter HTML semantique, contraste et focus visible | navigation clavier possible et structure lisible | Should |
| Rapport qualite | Exposer les controles de qualite des donnees | `/api/data-quality` retourne les controles du pipeline | Should |
| Lineage | Documenter la provenance des KPI | `/api/lineage` relie KPI Gold et sources Raw/Silver | Should |
| Gestion fine des droits | Ajouter roles et permissions par profil | controle d'acces documente pour version cible | Could |

## Exigences non fonctionnelles

| Exigence | Attendu |
|---|---|
| Reproductibilite | le README doit permettre de relancer le pipeline et l'API |
| Maintenabilite | le code est separe entre ingestion, transformation, API et web |
| Performance | le POC doit traiter les fichiers fournis localement en temps raisonnable |
| Tracabilite | les couches de donnees doivent rendre les transformations explicites |
| Accessibilite | le dashboard doit etre lisible, navigable au clavier et compatible avec les bases RGAA/WCAG |

## Conformite et accessibilite numerique

Normes de reference :

- RGAA : Referentiel General d'Amelioration de l'Accessibilite ;
- WCAG : Web Content Accessibility Guidelines.

Mesures prevues pour le dashboard :

- utiliser des balises HTML semantiques : `header`, `main`, `section`, titres hierarchises ;
- garantir un contraste suffisant entre texte et fond pour les KPI ;
- permettre la navigation clavier avec un focus visible ;
- fournir une zone de statut `role="status"` pour annoncer le chargement des KPI ;
- eviter de transmettre l'information uniquement par la couleur.

## A defendre

Le cahier des charges montre que le POC n'est pas juste un script. Il respecte une logique produit : ingestion, qualite, exposition API, interface accessible et documentation reproductible.
