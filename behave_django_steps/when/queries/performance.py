"""Steps for testing the performance of queries."""
import time

from behave import when


@when('I execute the step "{step}" it should only make "{query_count}" queries')
def check_query_count(context, step, query_count):
    """Check that the step only makes the expected number of queries."""
    with context.test.assertNumQueries(int(query_count)):
        context.execute_steps(step)


@when('I execute the step "{step}" it should only take "{max_seconds}" seconds')
def check_execution_time(context, step, max_seconds):
    """Check that the step only takes the specified time."""
    before = time.time()
    context.execute_steps(step)
    after = time.time()
    context.test.assertLessEqual(after - before, int(max_seconds))
