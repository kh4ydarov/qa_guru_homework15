import pytest
from selene import browser, have
from models.main_page import site


def test_desktop_version(driver):
    if browser.config.window_width and browser.config.window_height <= 1000:
        pytest.skip('Mobile version')
    else:
        site.open()
        site.desktop_sign_in()

def test_mobile_version(driver):
    if browser.config.window_width and browser.config.window_height >= 1080:
        pytest.skip('Desktop version')
    else:
        site.open()
        site.mobile_sign_in()