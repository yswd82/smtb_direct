# -*- coding: utf-8 -*-
from smtb_direct.core.locator import *


class BasePage:
    def __init__(self, driver):
        self._driver = driver


class LoginPage(BasePage):

    _locator = LoginPageLocator

    def click_login(self):
        element = self._driver.find_element(*self._locator.BUTTON_LOGIN)
        element.click()
