import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session.login(username="admin", password="secret")

    def final():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(final)
    return fixture
