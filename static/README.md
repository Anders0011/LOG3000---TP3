Dossier : static

Le dossier /static contient les fichiers statiques utilisés par l’application Flask,
c’est-à-dire les éléments qui ne changent pas pendant l’exécution du programme.
Dans ce projet, il sert principalement à gérer l’apparence visuelle de la calculatrice
web grâce au fichier style.css. Ce fichier joue un rôle essentiel dans la présentation
et l’ergonomie de l’application : il rend l’interface attrayante, claire et agréable
à utiliser pour l’utilisateur.

Le fichier style.css contrôle la disposition et le style des éléments de la page HTML.
Il définit un thème sombre qui permet un bon contraste avec le texte, tout en centrant
la calculatrice au milieu de l’écran pour une meilleure lisibilité. Il utilise le système
de grille (CSS Grid) pour organiser les boutons en quatre colonnes bien espacées, garantissant
une mise en page simple et cohérente. Ce fichier gère également les effets visuels lors
du survol et du clic sur les boutons afin d’améliorer l’expérience utilisateur.

Ce style ne dépend d’aucune bibliothèque externe comme Bootstrap : tout le design a été
créé à la main pour conserver un aspect sobre et professionnel. Le fichier style.css est
lié au fichier HTML principal grâce à la fonction url_for('static', filename='style.css')
fournie par Flask, ce qui permet au serveur de retrouver automatiquement le fichier dans
le dossier static. Ce dossier est un répertoire standard de Flask et il est chargé
automatiquement lorsque l’application est exécutée.

En résumé, le dossier /static définit l’identité visuelle du projet. Il assure la cohérence
graphique, le confort d’utilisation et la clarté de l’interface. Sans ce fichier, l’application
fonctionnerait toujours sur le plan logique, mais son apparence serait brute et peu intuitive.

