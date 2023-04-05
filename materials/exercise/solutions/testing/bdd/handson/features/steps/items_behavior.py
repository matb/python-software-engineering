from behave import given, then, when  # pylint: disable=no-name-in-module

import game.items


@given("the hero has {number:d} items")
def _given_items(context, number):
    item = game.items.Pan()
    for _ in range(number):
        context.hero.pick_up_item(item)


@when("the hero picks up a  new item")
def _add_one_more_item(context):
    context.hero.pick_up_item(game.items.Pan())


@then("he has {number:d} items")
def _evaluate_items(context, number):
    want = number
    got = len(context.hero.items)
    print(f" Want - {want}  | Got - {got}")
    assert want == got
