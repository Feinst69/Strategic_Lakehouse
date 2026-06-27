# Preparation a l'IA agentique

## Principe

Une IA appliquee a la business intelligence ne doit pas interroger directement des fichiers bruts disperses. Elle doit consommer des donnees fiables, documentees et gouvernees.

Le Lakehouse prepare cette trajectoire en separant :

- les donnees brutes en Bronze ;
- les donnees fiables en Silver ;
- les indicateurs metier en Gold ;
- l'exposition controlee via API.

## Exemple de cas d'usage futur

Un agent BI interne pourrait recevoir la question :

```text
Quel pays genere le plus de chiffre d'affaires et quelle categorie explique cette performance ?
```

Au lieu de lire les CSV sources, l'agent interrogerait :

```text
/api/kpis
/api/data-quality
/api/lineage
```

Il pourrait alors repondre avec un indicateur metier, un niveau de confiance et une explication de provenance.

## Garde-fous necessaires

Pour industrialiser cette approche, il faudrait ajouter :

- authentification et autorisations par profil ;
- catalogue de donnees ;
- documentation des KPI ;
- tests de qualite automatises ;
- journalisation des appels API ;
- masquage ou exclusion des donnees personnelles.

## A defendre

Le POC est IA-ready car il ne connecte pas l'IA a des silos instables. Il prepare une couche Gold stable, exposee par API, auditable par lineage et controlee par rapport qualite.
