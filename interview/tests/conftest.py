import pytest


@pytest.fixture(scope='session')
def setup_db(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        import database
