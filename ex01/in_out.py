def square(x: int | float) -> int | float:
    """
    Returns the square of a given number.

    Args:
    x (int | float): The number to square.

    Returns:
    int | float: The square of x.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Returns x raised to the power of itself.

    Args:
    x (int | float): The number to raise to its own power.

    Returns:
    int | float: The result of x ** x.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns a function that applies the given function
    to x and updates x on each call.

    Args:
    x (int | float): The initial value.
    function (callable): The function (like `square` or `pow`) to apply to x.

    Returns:
    object: A callable function that applies the given function
    to x on each call.
    """
    count = 0  # Initialize counter

    def inner() -> float:
        """
        Applies the function to x and updates x with the result on each call.

        Returns:
        float: The result of applying the function to x.
        """
        nonlocal x
        nonlocal count
        count += 1  # Increment the counter
        result = function(x)  # Apply the function to x
        x = result  # Update x with the result
        return result

    return inner
