Dossier : templates

Le dossier /templates contient les fichiers de modèles HTML utilisés par Flask pour afficher
les pages web. Contrairement aux fichiers statiques, les modèles HTML peuvent recevoir et
afficher des données dynamiques envoyées par le backend Python. Dans cette application, le
dossier contient le fichier principal index.html, qui représente l’interface de la
calculatrice web. Il s’agit du point d’interaction principal entre l’utilisateur et le
programme.

Le fichier index.html est chargé via la fonction render_template() dans app.py. Il contient
la structure complète de la calculatrice : un champ d’affichage, les boutons numériques, les
opérateurs et un bouton “C” pour effacer. L’élément d’entrée (<input>) affiche le résultat
calculé, transmis par le serveur Flask sous la forme d’une variable dynamique appelée
{{ result }}. Grâce à ce mécanisme, la page peut afficher immédiatement le résultat d’une
opération après que l’utilisateur a cliqué sur le bouton “=”.

Le document HTML intègre également un petit script JavaScript qui permet de remplir ou de
vider le champ d’affichage sans recharger la page. Ce script ajoute ou efface les caractères
saisis par l’utilisateur avant l’envoi du formulaire. Le fichier index.html est aussi relié
au fichier style.css pour assurer une mise en page harmonieuse et moderne. Cette connexion se
fait par le lien :
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
qui permet à Flask de retrouver le fichier CSS automatiquement.

En résumé, le dossier /templates contient la partie visible de l’application. Il fait le lien
entre l’utilisateur et la logique Python, en transformant les calculs en une interface claire,
intuitive et interactive. Sans ce fichier, l’application pourrait exécuter des calculs, mais
elle n’aurait aucun moyen d’afficher le résultat à l’écran.

