from new_student import Student


def main():
    """Main function to test the Student class."""

    try:
        student = Student(name="", surname="")
        print(student)

        student = Student(name="Edward", surname="agle", id="toto")
        print(student)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
