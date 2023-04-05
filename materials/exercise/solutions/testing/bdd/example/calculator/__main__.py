from calculator.calculator import Calculator


def main():
    """Program entry point."""
    calculator = Calculator()
    calculator.add_input(int(input()))
    calculator.add_input(int(input()))
    print(f"X = {calculator.sum()}")


if __name__ == "__main__":
    main()
