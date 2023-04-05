from behave import given, then, when  # pylint: disable=no-name-in-module

import game.items
import game.monsters


@given("the hero as a sword with {dmg:d} dmg and a wolf with {hp:d} HP")
def _given_dmg_and_hp(context, dmg, hp):
    context.hero.pick_up_item(game.items.Weapon("sword", 1,3,1))
    context.enemy = game.monsters.Wolf()


@when("he attacks the wolf {number:d} time")
def _attack_x_times(context, number):
    context.hero.attack("sword", context.enemy)


@then("the wolf has {hp:d} hp left")
def _evaluate_hp(context, hp):
    """
    Note: This test will fail once  - due to wrong implementation
    """
    want = hp
    got = context.enemy.hp
    assert want == got
