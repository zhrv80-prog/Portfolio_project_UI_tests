from time import sleep

import pytest
from selene import browser, have, be


def test_draft():
    browser.open('https://www.saucedemo.com/')
    browser.element('#user-name').click().type('standard_user')
    browser.element('#password').click().type('secret_sauce')
    browser.element('#login-button').click()
    browser.element('.title').should(be.visible)
    browser.quit()