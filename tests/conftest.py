import pytest
from selene import browser


@pytest.fixture
def desktop_version():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield
    browser.quit()


@pytest.fixture
def mobile_version():
    browser.config.window_width = 412
    browser.config.window_height = 915

    yield
    browser.quit()


@pytest.fixture(params=['desktop_version', 'mobile_version'])
def driver(request):
    if request.param == 'desktop_version':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    else:
        browser.config.window_width = 412
        browser.config.window_height = 915

    yield
    browser.quit()


@pytest.fixture(params=[(1920, 1080), (412, 915)])
def driver_setup(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

