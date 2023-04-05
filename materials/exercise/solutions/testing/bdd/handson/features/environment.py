from game.hero import Hero


def before_scenario(context, scenario):
    """Execute before each scenario."""
    context.hero = Hero(items=[])
