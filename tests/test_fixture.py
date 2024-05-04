from models.main_page import site


def test_github_desktop(desktop_version):
    site.open()
    site.desktop_sign_in()


def test_github_mobile(mobile_version):
    site.open()
    site.mobile_sign_in()

