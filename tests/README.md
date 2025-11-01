# Dossier `/tests`

##  Objectif
Ce dossier contient l’ensemble des **tests unitaires** du projet de calculatrice web.
Les tests ont pour but de garantir que les fonctions du backend (calculs et logique Flask)
fonctionnent correctement et qu’aucun bogue n’est introduit lors des modifications du code.

---

##  Structure des tests
- **test_operators.py**  
  Contient les tests unitaires des fonctions `add`, `subtract`, `multiply`, et `divide`.  
  Ces tests vérifient la justesse des résultats et la gestion des erreurs (par exemple, division par zéro).

- **test_calculate.py**  
  Contient les tests unitaires pour la fonction `calculate()` de `app.py`.  
  Ces tests valident la capacité du programme à interpréter correctement les expressions
  mathématiques fournies par l’utilisateur.

---

## Exécution des tests
Pour exécuter l’ensemble des tests, assurez-vous d’avoir **pytest** installé, puis exécutez la commande suivante à la racine du projet :

python -m pytest
