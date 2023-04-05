from calculator.calculator import Calculator  # pylint: disable=import-error


def before_scenario(context, scenario):
    """Execute before each scenario."""
    tags = set(scenario.tags + scenario.feature.tags)
    if "domain" in tags:
        context.calculator = Calculator()
