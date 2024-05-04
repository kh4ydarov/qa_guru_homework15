from selene import browser, have


class mainPage:
    def open(self):
        browser.open('https://github.com')
        return self

    def desktop_sign_in(self):
        browser.element('.HeaderMenu-link--sign-in').click()

    def mobile_sign_in(self):
        browser.element('.Button-label').click()
        browser.element('.HeaderMenu-link--sign-in').click()


site = mainPage()
