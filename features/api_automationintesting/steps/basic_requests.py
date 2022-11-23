from lib.api.automationintesting_api import AutomationInTestingAPIClient
from behave import given, when, then


@given('the client is authenticated')
def step_impl(context):
    context.client = AutomationInTestingAPIClient()
    # Please note that the user name and password would not be stored in code
    # but in a env variable this a demo user and password.
    username = "admin"
    password = "password123"
    context.client.get_token(username, password)


@when('the client requests the ping endpoint')
def step_impl(context):
    context.client = AutomationInTestingAPIClient()
    context.response = context.client.ping_endpoint()


@when('the client requests "{endpoint}" for id "{id}"')
def step_impl(context, endpoint, id):
    context.response = context.client.get_booking_id_endpoint(endpoint, id)


@then('the request will return "{status_code}" status code')
def step_impl(context, status_code):
    expected_status = (int(status_code))
    actual_status = context.response['status']
    assert actual_status == expected_status, (
        f'Expected status code {expected_status}, got {actual_status}.'
    )


@then('the request will return "{firstname}" firstname')
def step_impl(context, firstname):
    expected_name = (str(firstname))
    data = context.response['body']
    if expected_name not in data:
        raise Exception(f'firtname name: {expected_name} not found')
