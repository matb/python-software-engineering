class Calculator:
    """A helper for math novices."""

    def __init__(self):
        """Initialize calculator object."""
        self.numbers = []

    def add_input(self, value):
        """Add a new input to the calculator."""
        self.numbers.append(value)

    def sum(self):
        """Sum two numbers."""
        return self.numbers.pop() + self.numbers.pop()
