from typing import Any


def callLimit(limit: int):
    """Decorator to limit the number of times a function can be called."""

    count = 0

    def callLimiter(function):
        """
        Wrapper function to limit the number of times a function can be called.
        """

        def limit_function(*args: Any, **kwds: Any):
            """
            Function to limit the number of times a function can be called.
            """

            nonlocal count

            if count < limit:
                result = function(*args, **kwds)
                count += 1
                return result

            print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter