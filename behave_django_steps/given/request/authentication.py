"""Authentication steps."""
from behave import given
import base64
from rest_framework import HTTP_HEADER_ENCODING
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

User = get_user_model()


def basic_auth_header(username: str, password: str) -> str:
    """Return a dict with the basic auth header."""

    credentials = f'{username}:{password}'
    base64_credentials = base64.b64encode(credentials.encode(HTTP_HEADER_ENCODING)).decode(HTTP_HEADER_ENCODING)
    return f'Basic {base64_credentials}'


@given("I am a superuser")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    user = User.objects.create_user(
        username='test superuser',
        password='test',
        is_active=True,
        is_staff=True,
        is_superuser=True
    )
    context.user = user
    context.test.client.force_login(user)


@given("I am a registered user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    user = User.objects.create_user(
        username='test user',
        password='test',
        is_active=True,
        is_staff=False,
        is_superuser=False
    )
    context.user = user
    context.test.client.force_login(user)


@given("I am a staff user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    user = User.objects.create_user(
        username='test staff user',
        password='test',
        is_active=True,
        is_staff=True,
        is_superuser=False
    )
    context.user = user
    context.test.client.force_login(user)


@given("I am an anonymous user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.user = AnonymousUser()
    context.credentials = basic_auth_header('test', 'bad_password')
