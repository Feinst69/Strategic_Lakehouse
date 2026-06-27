# Synthese diagnostic du SI GlobalTrade Solutions

## Contexte

GlobalTrade Solutions dispose d'un systeme d'information fragmente. Les donnees utiles a l'analyse commerciale sont reparties entre un ERP on-premise, un CRM SaaS et des fichiers analytiques produits localement. Cette organisation limite la capacite de l'entreprise a produire des indicateurs fiables, comparables et accessibles a la demande.

Le POC s'appuie sur trois familles de donnees :

- `g_fact_sales.csv` : ventes historiques issues du silo ERP ;
- `g_dim_products.csv` : referentiel produits issu du silo ERP ;
- `g_dim_customers.csv` : referentiel clients issu du silo CRM ;
- exports derives : agregats de ventes par pays, categorie ou mois en couche Gold.

## Cartographie fonctionnelle

| Domaine | Donnees principales | Acteurs metier | Probleme actuel |
|---|---|---|---|
| Ventes | commandes, chiffre d'affaires, quantites, dates | direction commerciale, COMEX, data analysts | les ventes sont analysees separement des clients et des produits |
| Produits | produit, categorie, sous-categorie, cout | achats, supply chain, controle de gestion | le referentiel produit n'est pas toujours relie aux analyses BI |
| Clients | identite, pays, genre, date de creation | marketing, service client, CRM managers | la vision client reste separee de l'historique d'achat |
| Analyse BI | KPI, exports, tableaux de bord | direction, managers metier | les indicateurs sont produits par extraction manuelle ou locale |

## Cartographie applicative

| Application ou source | Role | Type de silo | Impact analytique |
|---|---|---|---|
| GlobalTrade ERP | gere les ventes, produits et stocks | on-premise historique | donnees critiques mais peu accessibles pour la BI moderne |
| GlobalTrade CRM Cloud | gere les clients et interactions commerciales | SaaS externe | rupture entre donnees client et donnees de vente |
| Fichiers analytiques | exports CSV/Parquet manipules localement | fichiers non gouvernes | risque de versions multiples et d'indicateurs contradictoires |
| Strategic Lakehouse | centralise, fiabilise et expose les donnees | architecture cible | fournit une base unifiee pour BI et futurs usages IA |

## Constats de silotage

Le SI actuel cree plusieurs difficultes :

- absence de source analytique unique pour les ventes, les clients et les produits ;
- duplication des exports et risque d'ecarts entre indicateurs ;
- faible tracabilite des transformations appliquees aux donnees ;
- dependance aux manipulations manuelles ;
- difficulte a exposer des KPI fiables via API ou dashboard ;
- frein a l'arrivee de futures couches IA-agentiques, qui necessitent des donnees gouvernees, documentees et structurees.

## Impacts sur la chaine de valeur analytique

La fragmentation ralentit toute la chaine BI. Les donnees doivent d'abord etre retrouvees, exportees, nettoyees puis rapprochees avant de produire un indicateur. Ce temps de preparation reduit la valeur des analyses et augmente le risque d'erreur.

Pour un utilisateur metier, l'impact est concret : deux equipes peuvent presenter deux chiffres d'affaires differents selon l'export utilise. Pour un utilisateur en situation de handicap, cette fragmentation peut aussi compliquer l'acces a l'information si les donnees ne sont disponibles que dans des fichiers peu accessibles ou des outils heterogenes.

## Approche data-driven proposee

L'approche cible consiste a mettre en place un Lakehouse en trois couches :

- Bronze : ingestion des donnees brutes issues des silos ;
- Silver : nettoyage, typage, dedoublonnage et standardisation ;
- Gold : donnees agregees et pretes pour les usages BI.

Cette approche permet de conserver la tracabilite des donnees, d'ameliorer progressivement leur qualite et de fournir des KPI fiables via API. Elle prepare aussi l'entreprise a des usages IA futurs, car les agents ou modeles pourront s'appuyer sur des donnees structurees et gouvernees.

## A defendre

Le probleme n'est pas seulement technique. Il s'agit d'un probleme de gouvernance et de valeur metier : tant que les donnees restent dispersees, l'entreprise ne peut pas automatiser la BI ni industrialiser des usages IA fiables.
