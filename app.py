"""Small command-line calculator application."""

from __future__ import annotations

import argparse
from collections.abc import Callable


Number = int | float


def addition(a: Number, b: Number) -> Number:
    """Return the sum of two numbers."""
    return a + b


def soustraction(a: Number, b: Number) -> Number:
    """Return the difference between two numbers."""
    return a - b


def multiplication(a: Number, b: Number) -> Number:
    """Return the product of two numbers."""
    return a * b


def division(a: Number, b: Number) -> float:
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("La division par zéro est impossible.")
    return a / b


OPERATIONS: dict[str, Callable[[Number, Number], Number]] = {
    "addition": addition,
    "soustraction": soustraction,
    "multiplication": multiplication,
    "division": division,
}


def calculer(operation: str, a: Number, b: Number) -> Number:
    """Apply a named operation to two numbers."""
    try:
        fonction = OPERATIONS[operation]
    except KeyError as error:
        operations = ", ".join(OPERATIONS)
        raise ValueError(
            f"Opération inconnue : {operation}. Choisissez parmi : {operations}."
        ) from error
    return fonction(a, b)


def main() -> None:
    """Run the calculator command-line interface."""
    parser = argparse.ArgumentParser(description="Une petite calculatrice.")
    parser.add_argument("operation", choices=OPERATIONS)
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)
    args = parser.parse_args()
    print(calculer(args.operation, args.a, args.b))


if __name__ == "__main__":
    main()