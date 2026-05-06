"""Module for solving the 24 game using a recursive approach."""


def _generate_operations(value1, expression1, value2, expression2):
    """
    Generate valid mathematical operations for a pair of numbers.

    Parameters
    ----------
    value1 : int
        The numeric value of the first operand.
    expression1 : str
        The string representation of the first operand's equation.
    value2 : int
        The numeric value of the second operand.
    expression2 : str
        The string representation of the second operand's equation.

    Yields
    ------
    tuple
        A tuple containing (new_integer_value, new_string_expression).
    """
    yield value1 + value2, f"({expression1} + {expression2})"
    yield value1 * value2, f"({expression1} * {expression2})"

    if value1 - value2 >= 0:
        yield value1 - value2, f"({expression1} - {expression2})"

    if value2 != 0 and value1 % value2 == 0:
        yield value1 // value2, f"({expression1} / {expression2})"


def _recurse(state, target, solutions):
    """
    Recursively evaluate combinations of numbers to reach the target.

    Parameters
    ----------
    state : list of tuple
        The current pool of available numbers, as (value, expression).
    target : int
        The target integer to reach.
    solutions : set
        A set collecting all unique, valid string equations.
    """
    if len(state) == 1:
        value, expression = state[0]
        if value == target:
            solutions.add(expression)
        return

    n = len(state)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            value1, expression1 = state[i]
            value2, expression2 = state[j]

            remaining = [state[k] for k in range(n) if k not in (i, j)]

            for new_val, new_expr in _generate_operations(
                value1, expression1, value2, expression2
            ):
                _recurse(remaining + [(new_val, new_expr)], target, solutions)


def solve_24(numbers, target=24):
    """
    Find all valid equations combining a list of numbers to reach a target.

    Parameters
    ----------
    numbers : list of int
        The starting integers to be evaluated.
    target : int, optional
        The mathematical target to reach (default is 24).

    Returns
    -------
    list of str
        A list of unique mathematical expressions evaluating to the target.
    """
    initial_state = [(n, str(n)) for n in numbers]
    solutions = set()

    _recurse(initial_state, target, solutions)

    return list(solutions)
