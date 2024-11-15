from typing import Any
from math import sqrt


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate statistical measures, including mean, median, quartile,
    standard deviation, and variance, based on the provided  arguments.
    It supports keyword arguments to request specific statistical
    measures for printing.

    Parameters:
    *args (Any): Variable number of positional arguments
    representing values for calculations.
    **kwargs (Any): Keyword arguments indicating the
    requested statistical measures for printing.

    Returns:
    None: The function doesn't return any value.
    It prints the requested statistical measures."""

    def mean(ls: list[int | float]) -> float:
        """Calculate the Mean"""
        return sum(ls) / len(ls)

    def median(ls: list[int | float]) -> int | float:
        """Calculate the Median"""
        if len(ls) == 1:
            return ls[0]
        else:
            s = sorted(ls)
            mid = int(len(s)/2)
            return s[mid] if len(ls) % 2 else (s[mid - 1] + s[mid])/2

    def var(ls: list[int | float]) -> float:
        """Calculate the Population Variance"""
        _mean = mean(ls)
        return mean([(x - _mean) ** 2 for x in ls])

    def std(ls: list[int | float]) -> float:
        """Calculate the Standard Deviation"""
        return sqrt(var(ls))

    def quartile(ls: list[int | float]) -> list[float]:
        """Calculate Quartile (25% and 75%)"""
        if len(ls) == 1:
            return [float(ls[0]), float(ls[0])]
        s = sorted(ls)
        mid = int(len(s)/2)
        m1 = mid + 1 if len(s) % 2 else mid
        return [float(median(s[:m1])), float(median(s[mid:]))]

    def do_op(op: str, ls: list[int | float]) -> None:
        # Verificar si `ls` está vacío
        if len(ls) == 0:
            print("ERROR")
        else:
            # Diccionario para asignar la operación correspondiente
            operations = {
                            "mean": mean,
                            "median": median,
                            "quartile": quartile,
                            "std": std,
                            "var": var
                        }
            # Verificar si la operación es válida
            if operations.get(op):
                print(f"{op} : {operations.get(op)(ls)}")
            else:
                print("ERROR")

    # Filtrar y validar valores numéricos en `*args`
    nums = [x for x in args if isinstance(x, (int, float))]

    # Comprobación si `kwargs` contiene claves válidas
    valid_ops = {"mean", "median", "quartile", "std", "var"}
    if not any(k in valid_ops for k in kwargs.values()):
        print("ERROR")
        return

    # Ejecutar operaciones solicitadas
    [do_op(kwargs[k], nums) for k in kwargs if kwargs[k] in valid_ops]
