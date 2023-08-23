import pytest


@pytest.mark.django_db
@pytest.mark.usefixtures('setup_db')
class BaseDBTestCase:
    pass
