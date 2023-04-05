class Summer:
    """A helper for math novices."""

    def __init__(self):
        """Initialize calculator object."""
        self.numbers = []

    def add_input(self, value):
        """Add a new input to the calculator."""
        self.numbers.append(value)

    def sum(self):
        """Sum two numbers."""
        if len(self.numbers) != 2:
            raise ValueError("Numbers has to contain two numbers - no more no less ")
        return self.numbers.pop() + self.numbers.pop()
