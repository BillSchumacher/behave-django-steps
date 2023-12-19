"""Response data steps."""
from behave import then


@then("values exist in the response")
def response_values_exist(context):
    """Check that values exist in the response."""
    context.test.assertTrue(context.table)
    context.test.assertTrue(context.table[0].as_dict())
    for row in context.table:
        for key, value in row.as_dict().items():
            response_value = context.response.data.get(key)
            if isinstance(response_value, list):
                context.test.assertIn(value, response_value)
            else:
                context.test.assertEqual(
                    response_value, value, f"Key: {key}, Value: {value}"
                )


@then('values exist in "{response_key}" in the response')
def response_values_exist_at_key(context, response_key):
    """Check that values exist in the response."""
    context.test.assertTrue(context.table)
    context.test.assertTrue(context.table[0].as_dict())
    data = context.response.data.get(response_key, {})
    for row in context.table:
        for key, value in row.as_dict().items():
            if isinstance(data, list):
                found = False
                for item in data:
                    response_value = item.get(key)
                    if response_value == value:
                        found = True
                        break
                context.test.assertTrue(found)
            else:
                response_value = data.get(key)
                response_type = type(response_value)
                if not isinstance(value, response_type):
                    if response_type == bool:
                        value = value == "True"
                    elif response_type is type(None):
                        value = None if value in ["", "None"] else value
                    elif response_type != dict:
                        value = type(response_value)(value)
                context.test.assertEqual(
                    response_value, value, f"Key: {key}, Value: {value}"
                )
