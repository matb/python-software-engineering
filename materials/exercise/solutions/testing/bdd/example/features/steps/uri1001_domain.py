from behave import given, when  # pylint: disable=no-name-in-module
@given("the first number is {number:d}")
def _given_first_number(context, number):
    context.calculator.add_input(number)


@given("the second number is {number:d}")
def _given_second_number(context, number):
    context.calculator.add_input(number)


@when("the two numbers are added")
def _when_two_numbers_are_added(context):
    context.result = context.calculator.sum()
