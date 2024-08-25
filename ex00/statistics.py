import numpy as np


def ft_statistics(*args: int, **kwargs: str) -> None:
    """def ft_statistics(*args: int, **kwargs: str)"""
    for key, value in kwargs.items():
        if (len(args) == 0):
            print("ERROR")
            continue
        if (value == "mean"):
            print(f"mean : {np.mean(args)}")
        elif (value == "median"):
            print(f"median : {np.median(args):.0f}")
        elif (value == "quartile"):
            quantile = np.quantile(args, [0.25, 0.75])
            print(f"quartile : [{quantile[0]}, {quantile[1]}]")
        elif (value == "std"):
            print(f"std {np.std(args)}")
        elif (value == "var"):
            print(f"var {np.var(args)}")