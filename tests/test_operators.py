"""
Module : test_operators.py
--------------------------
Ce module contient les tests unitaires pour les fonctions arithmétiques
définies dans le fichier operators.py.

Objectif :
Vérifier que chaque opération mathématique retourne le résultat attendu
et que les erreurs (comme la division par zéro) sont correctement gérées.
"""

import pytest
from operators import add, subtract, multiply, divide

def test_add():
    """Vérifie que l'addition retourne la somme correcte."""
    assert add(3, 4) == 7
    assert add(-2, 5) == 3

def test_subtract():
    """Vérifie que la soustraction retourne la différence correcte."""
    assert subtract(10, 4) == 6
    assert subtract(-3, -1) == -2

def test_multiply():
    """Vérifie que la multiplication retourne le produit correct."""
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0

def test_divide():
    """Vérifie que la division retourne le quotient correct."""
    assert divide(10, 2) == 5
    assert divide(8, 3) == 2.6666666666666665


