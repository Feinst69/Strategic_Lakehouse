# Recommandation strategique

## Recommandation

Nous recommandons a GlobalTrade Solutions d'adopter une architecture Lakehouse afin de moderniser progressivement son systeme d'information analytique. Cette architecture permet de centraliser les donnees issues de l'ERP, du CRM et des fichiers analytiques tout en conservant une separation claire entre donnees brutes, donnees fiabilisees et donnees pretes pour la BI.

Le Lakehouse n'est pas uniquement une solution technique. C'est une trajectoire de maturite data-driven. Il permet de passer d'une logique d'exports locaux et de retraitements manuels a une logique de donnees gouvernees, reutilisables et exposees sous forme de services.

## Argument 1 : unification progressive des silos

Le SI actuel repose sur plusieurs sources separees : ERP on-premise, CRM SaaS et fichiers analytiques. Cette situation produit des ruptures dans la chaine de valeur analytique. Une architecture Lakehouse permet d'integrer ces sources sans exiger leur remplacement immediat.

Dans le POC, cette logique est demontree par l'ingestion des ventes, produits et clients dans une couche Bronze, puis par leur rapprochement progressif jusqu'a une table Gold `enriched_sales`. Le Lakehouse devient ainsi un point de convergence entre applications existantes et usages analytiques.

## Argument 2 : qualite, tracabilite et gouvernance des donnees

La separation Bronze / Silver / Gold permet de rendre les transformations explicites. Les donnees brutes sont conservees, les donnees Silver sont nettoyees et typees, puis les donnees Gold sont agregees pour la BI.

Cette organisation renforce la gouvernance : il devient possible d'expliquer d'ou vient un KPI, quelles transformations ont ete appliquees et quelle couche doit etre utilisee selon le besoin. Elle facilite aussi la conformite RGPD, car les controles d'acces et les regles de minimisation peuvent etre appliques par couche.

## Argument 3 : preparation aux futurs usages IA et BI agentique

Les futures couches IA-agentiques ne pourront produire des recommandations fiables que si elles s'appuient sur des donnees structurees, documentees et controlees. Le Lakehouse fournit cette base.

Dans le POC, les KPI sont exposes via une API FastAPI. Cette API pourrait demain etre consommee par un dashboard avance, un agent conversationnel interne ou un outil de pilotage commercial. L'entreprise evite ainsi de connecter directement l'IA a des fichiers disperses ou a des bases non gouvernees.

## Conclusion

Le Lakehouse est recommande car il repond a trois enjeux strategiques : unifier les silos sans casser l'existant, fiabiliser la chaine analytique et preparer l'entreprise a l'IA. Pour GlobalTrade Solutions, c'est l'architecture la plus coherente avec une evolution data-driven progressive, gouvernee et demonstrable.

## A defendre

La phrase cle : le Lakehouse transforme des donnees dispersees en actifs analytiques gouvernes. Il ne remplace pas tout le SI, il cree une couche d'intelligence au-dessus de l'existant.
