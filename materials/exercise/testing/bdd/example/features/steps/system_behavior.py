import subprocess

from behave import given, then, when  # pylint: disable=no-name-in-module


@given("the input is")
def _given_input(context):
    context.stdin_data = context.text


@when('the program "{program}" runs')
def _when_program_runs(context, program):
    context.result = subprocess.run(
        ["python", "-m", program],
        capture_output=True,
        check=True,
        text=True,
        input=context.stdin_data,
    )


@then("the output should be")
def _then_output_should_be(context):
    # Python's bytes.splitlines use the 'universal newlines' approach
    # so that specific line break characters are not relevant, but a
    # line break is.
    expected = context.text.splitlines()
    observed = context.result.stdout.splitlines()
    assert expected == observed
