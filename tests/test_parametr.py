import pytest
from models.main_page import site


@pytest.mark.parametrize('driver', ['desktop_version'], indirect=True)
def test_github_desktop(driver):
    site.open()
    site.desktop_sign_in()


@pytest.mark.parametrize('driver', ['mobile_version'], indirect=True)
def test_github_mobile(driver):
    site.open()
    site.mobile_sign_in()
