# Comparatif des architectures cibles

## Tableau de comparaison

| Critere | Data Warehouse Cloud | Data Lake | Lakehouse |
|---|---|---|---|
| Objectif principal | BI structuree et reporting | stockage massif de donnees brutes | unification BI, data science et IA |
| Cout | eleve si volumetrie et requetes importantes | faible pour le stockage, plus variable pour le traitement | intermediaire, optimise par separation stockage/calcul |
| Scalabilite | bonne, mais souvent dependante du fournisseur | tres forte sur donnees volumineuses | tres forte avec gouvernance et formats ouverts |
| Latence | bonne pour requetes SQL preparees | variable selon moteurs et qualite des donnees | bonne pour BI si couches Silver/Gold bien modelisees |
| Gouvernance | forte sur donnees structurees | faible si absence de catalogue et regles | forte si medallion architecture, catalogue et controle d'acces |
| Conformite RGPD | facilitee par schema clair et controles | plus risquee si donnees brutes non classees | adaptee avec separation des couches et politiques d'acces |
| Aptitude IA | limitee aux donnees structurees | forte pour exploration, mais qualite variable | tres adaptee car combine donnees fiables, historisation et flexibilite |
| Cas d'usage ideal | reporting financier, tableaux de bord standardises | stockage brut, data science exploratoire | BI moderne, IA-ready, gouvernance progressive |

## Analyse

Le Data Warehouse Cloud est performant pour du reporting classique, mais il impose souvent de structurer fortement les donnees avant ingestion. Dans le cas de GlobalTrade, cela risque de reproduire une logique rigide et couteuse, peu adaptee aux sources heterogenes.

Le Data Lake est attractif pour stocker de grands volumes de donnees brutes. En revanche, sans discipline de gouvernance, il peut devenir un simple depot de fichiers difficile a exploiter. Pour GlobalTrade, ce risque est important car le SI est deja fragmente.

Le Lakehouse combine les avantages des deux modeles. Il permet de stocker les donnees brutes, de les fiabiliser progressivement, puis de produire des tables Gold directement consommables par la BI, les API et les futurs cas d'usage IA.

## Choix retenu

Le Lakehouse est le meilleur choix pour GlobalTrade Solutions, car il repond simultanement aux besoins de consolidation, de gouvernance, de BI et de preparation a l'IA. Il apporte une trajectoire progressive sans imposer une refonte totale immediate du SI existant.

## A defendre

Le Data Warehouse est efficace mais trop rigide pour des silos heterogenes. Le Data Lake est flexible mais trop risque sans gouvernance. Le Lakehouse est le compromis strategique : il garde la flexibilite du lake et ajoute la fiabilite attendue pour la BI.
