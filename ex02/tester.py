from callLimit import callLimit


@callLimit(3)
def f():
    print("f()")


@callLimit(1)
def g():
    print("g()")


def main():
    """Main function to test the callLimit function."""

    try:
        for i in range(3):
            f()
            g()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
