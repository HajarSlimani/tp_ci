import pytest

from app import addition, calculer, division, multiplication, soustraction


def test_addition():
    assert addition(2, 3) == 5


def test_soustraction():
    assert soustraction(8, 3) == 5


def test_multiplication():
    assert multiplication(4, 2.5) == 10


def test_division():
    assert division(9, 3) == 3


def test_division_par_zero():
    with pytest.raises(ValueError, match="division par zéro"):
        division(5, 0)


@pytest.mark.parametrize(
    ("operation", "expected"),
    [
        ("addition", 7),
        ("soustraction", 3),
        ("multiplication", 10),
        ("division", 2.5),
    ],
)
def test_calculer(operation, expected):
    assert calculer(operation, 5, 2) == expected


def test_calculer_operation_inconnue():
    with pytest.raises(ValueError, match="Opération inconnue"):
        calculer("puissance", 2, 3)
