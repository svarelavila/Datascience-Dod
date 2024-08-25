def square(x: int | float) -> int | float:
    """Function to calculate the square of a number."""

    return x ** 2


def pow(x: int | float) -> int | float:
    """Function to calculate the power of a number."""

    return x ** x


def outer(x: int | float, function) -> object:
    """
    Function to return a function that will apply the given function to the
    given number.
    """

    count = 0

    def inner() -> float:
        """Inner function to apply the given function to the given number."""

        nonlocal count
        count = function(count) if count else function(x)
        return count

    return inner
