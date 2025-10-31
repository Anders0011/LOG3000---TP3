from flask import Flask, request, render_template
from app.operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Évalue une expression arithmétique simple contenant un seul opérateur.

    Exemple :
        "3+4" → 7
        "10/2" → 5.0

    Paramètres :
        expr (str): l’expression mathématique entrée par l’utilisateur.

    Retour :
        float : le résultat de l’opération.

    Exceptions :
        ValueError : si l’expression est vide, invalide, ou contient plus d’un opérateur.
    """
    # Vérifie que l’entrée est une chaîne de caractères non vide
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Supprime les espaces pour simplifier le traitement
    s = expr.replace(" ", "")

    op_pos = -1      # Position de l'opérateur dans la chaîne
    op_char = None   # Type d'opérateur trouvé (+, -, *, /)

    # Recherche de l'opérateur dans l'expression
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                # Si un deuxième opérateur est trouvé → erreur
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Vérifie la validité de la position de l'opérateur
    if op_pos <= 0 or op_pos >= len(s) - 1:
        # L’opérateur est au début, à la fin, ou absent
        raise ValueError("invalid expression format")

    # Sépare les deux opérandes autour de l’opérateur
    left = s[:op_pos]
    right = s[op_pos + 1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    # Exécute l'opération correspondante via le dictionnaire OPS
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l'application Flask.
    Affiche la page web de la calculatrice et traite les requêtes utilisateur.

    Méthodes HTTP :
        - GET  : affiche la page vide.
        - POST : lit l’expression envoyée par le formulaire, calcule le résultat
                 et l’affiche sur la même page.

    Retour :
        HTML rendu par le template index.html avec le résultat du calcul.
    """
    result = ""

    if request.method == 'POST':
        # Récupère la valeur du champ "display" dans le formulaire
        expression = request.form.get('display', '')

        try:
            result = calculate(expression)
        except Exception as e:
            # En cas d’erreur (ex. division par zéro, syntaxe invalide), afficher le message
            result = f"Error: {e}"

    # Affiche la page web avec le résultat du calcul
    return render_template('index.html', result=result)


if __name__ == '__main__':
    # Lancement du serveur Flask en mode debug (utile pour le développement)
    app.run(debug=True)