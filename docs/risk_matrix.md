# Matrice des risques

| Risque | Probabilite | Impact | Niveau | Mitigation concrete |
|---|---|---|---|---|
| Non-conformite RGPD | Moyenne | Eleve | Eleve | classifier les donnees personnelles, limiter l'exposition en Gold, appliquer des droits d'acces par profil |
| Perte de donnees | Faible a moyenne | Eleve | Eleve | conserver les donnees brutes en Bronze, automatiser les sauvegardes, journaliser les executions de pipeline |
| Indisponibilite de l'API BI | Moyenne | Moyen | Moyen | surveiller l'API, prevoir un mode degrade avec fichiers Gold statiques, documenter une procedure de redemarrage |
| Acces non autorise aux donnees | Moyenne | Eleve | Eleve | ajouter authentification, autorisation par role, separation des donnees sensibles et audit des acces |
| Dette technique | Moyenne | Moyen | Moyen | separer les modules, documenter le README, ajouter des tests automatises et standardiser les transformations |
| Mauvaise qualite des donnees sources | Elevee | Eleve | Eleve | appliquer controles Silver, rejeter les lignes invalides, produire des rapports d'anomalies |
| Dashboard peu accessible | Moyenne | Moyen | Moyen | appliquer RGAA/WCAG, tester le contraste, permettre navigation clavier et compatibilite lecteur d'ecran |

## Risques prioritaires

Les risques les plus critiques sont la non-conformite RGPD, les acces non autorises et la mauvaise qualite des donnees sources. Ils touchent directement la confiance dans le systeme analytique et la capacite de GlobalTrade a industrialiser des usages BI ou IA.

## A defendre

La matrice montre que la modernisation data ne consiste pas seulement a centraliser les donnees. Elle impose aussi de maitriser les risques de securite, de qualite, d'accessibilite et de conformite.
