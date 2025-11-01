"""
Module : test_calculate.py
--------------------------
Ce module teste la fonction calculate() du fichier app.py.

Objectif :
S'assurer que l'interpréteur d'expressions mathématiques fonctionne
correctement, même en cas d'erreur ou d'entrée invalide.
"""

import pytest
from app import calculate

def test_addition_expression():
    """Vérifie que l’expression d’addition retourne le bon résultat."""
    assert calculate("3+4") == 7

def test_subtraction_expression():
    """Vérifie que la soustraction fonctionne correctement."""
    assert calculate("10-5") == 5

def test_multiplication_expression():
    """Vérifie que la multiplication fonctionne correctement."""
    assert calculate("2*6") == 12

def test_division_expression():
    """Vérifie que la division fonctionne correctement."""
    assert calculate("8/2") == 4 

def test_invalid_expression_format():
    """Vérifie que les expressions mal formées lèvent une erreur."""
    with pytest.raises(ValueError):
        calculate("3++4")

def test_empty_expression():
    """Vérifie qu'une expression vide lève une erreur."""
    with pytest.raises(ValueError):
        calculate("")

def test_non_numeric_operands():
    """Vérifie que des opérandes non numériques lèvent une erreur."""
    with pytest.raises(ValueError):
        calculate("a+b")

def test_invalid_operator_position():
    """
    Vérifie que la fonction `calculate()` lève une erreur lorsque
    l'opérateur est mal positionné :
    - au début de l'expression,
    - à la fin de l'expression,
    - ou absent.
    """
    # opérateur au début
    with pytest.raises(ValueError):
        calculate("+5")

    # opérateur à la fin
    with pytest.raises(ValueError):
        calculate("8-")

    # aucun opérateur présent
    with pytest.raises(ValueError):
        calculate("1234")