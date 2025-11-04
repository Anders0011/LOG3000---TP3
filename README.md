# LOG3000---TP3 

Devoir #3 - Calculatrice Web

Équipe #11 
Anders Antoine 
Ayoub Issiakhem 
Elias Ladaa 

Objectif:  
L’objectif de ce projet est de créer une calculatrice web simple en utilisant la bibliothèque Flask de Python.
Le but est d’appliquer de bonnes pratiques de développement logiciel, incluant la gestion de versions avec GitHub, la documentation du code, l’ajout de tests unitaires et la correction de bogues.
L’application permet d’effectuer les opérations arithmétiques de base (addition, soustraction, multiplication et division) à travers une interface web intuitive. 

Portée du projet:
Le projet comporte trois composantes principales :
Backend (Python / Flask) – gère la logique de calcul et les requêtes HTTP.
Frontend (HTML / CSS) – affiche l’interface de la calculatrice.
Tests unitaires (pytest) – valident le bon fonctionnement des fonctions arithmétiques et du serveur Flask.
L’application est divisée en modules clairs et documentés pour faciliter la compréhension et la collaboration entre les membres de l’équipe.

Prérequis d'installation: 
Il faut avoir python 3.10 et pip installés sur son ordinateur afin de pouvoir lancer le projet. Il faut aussi avoir git installé pour pouvoir cloner le projet. 

Instructions d'installation: 
1. Il faut cloner le dépot dans le répertoire de son choix.
2. Créer un environnement virtuel dans le projet. 
- python -m venv venv 
- venv\Scripts\Activate ou source venv/bin/activate (sous linux)
3. Installer les dépendances nécessaires  
- pip install flask pytest
4. Lancer l'application  

Instructions d’utilisation:

Une fois l’application ouverte, l’utilisateur peut :
Entrer une expression (ex. 4+5, 9/3, 6*7) à l’aide des boutons de la calculatrice.
Appuyer sur = pour afficher le résultat.
Appuyer sur C pour effacer l’écran.
En cas d’erreur (par exemple, une expression invalide), un message d’erreur s’affiche à l’écran. 

Tests:

Le dossier /tests contient les fichiers de tests unitaires pour valider les fonctions de calcul et la logique Flask.
Pour exécuter les tests, utiliser la commande suivante :

pytest ou python -m pytest

Les tests couvrent notamment :
Les opérations arithmétiques (add, subtract, multiply, divide)
Les erreurs de saisie dans la fonction calculate()
Le bon fonctionnement du serveur Flask 

Flux de contribution (branches, PR, issues):

Le projet utilise un flux Git structuré pour assurer une bonne collaboration :

main : version stable et testée du projet.
bugfix/ : correction de bogues détectés par les tests.

Chaque bogue détecté est documenté dans une Issue GitHub avec :

une description du problème,
les étapes pour le reproduire,
et l’assignation à un membre responsable.

Les correctifs sont effectués sur une branche dédiée avant d’être validés via une Pull Request (PR).



