# RGPD et minimisation des donnees

## Principe applique

Le POC applique un principe de minimisation des donnees dans la couche Gold. Les tables Silver peuvent contenir des informations client detaillees, mais les sorties BI exposees ne doivent contenir que les champs necessaires a l'analyse.

## Donnees client non exposees en Gold

Les champs suivants ne sont pas exposes dans les KPI API :

- `first_name` ;
- `last_name` ;
- `birth_date` ;
- `customer_number`.

## Donnees client conservees pour l'analyse

La table Gold enrichie conserve uniquement des attributs utiles a l'analyse agregee :

- `customer_key` ;
- `country` ;
- `gender`.

## Justification

Le dashboard BI n'a pas besoin d'identifier directement les personnes pour afficher le chiffre d'affaires, le panier moyen ou le top pays. En limitant les donnees exposees, on reduit le risque de fuite de donnees personnelles et on facilite la conformite RGPD.

## A defendre

La couche Gold applique une logique de minimisation : elle donne aux metiers les indicateurs necessaires sans exposer d'identifiants personnels directs.
