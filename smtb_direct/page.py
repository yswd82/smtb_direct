# -*- coding: utf-8 -*-
from smtb_direct.locator import *
import mojimoji


class BasePage:
    def __init__(self, driver):
        self._driver = driver


class LoginPage(BasePage):
    _locator = LoginPageLocator()

    def input_member(self, member_num):
        element = self._driver.find_element(*self._locator.INPUT_MEMBER)
        element.send_keys(member_num)

    def input_password(self, password):
        element = self._driver.find_element(*self._locator.INPUT_PASSWORD)
        element.send_keys(password)

    def click_login(self):
        element = self._driver.find_element(*self._locator.BUTTON_LOGIN)
        element.click()
        return MenuPage(self._driver)


class MenuPage(BasePage):
    _locator = MenuPageLocator()

    def click_logout(self):
        element = self._driver.find_element(*self._locator.BUTTON_LOGOUT)
        element.click()

    def click_transaction(self):
        element = self._driver.find_element(*self._locator.BUTTON_TRANSACTION)
        element.click()
        return TransactionPage(self._driver)


class TransactionPage(BasePage):
    _locator = TransactionPageLocator()

    def click_transfer(self):
        element = self._driver.find_element(*self._locator.BUTTON_TRANSFER)
        element.click()
        return TransferPage(self._driver)


class TransferPage(BasePage):
    _locator = TransferPageLocator()

    def select_check(self, number):
        element = self._driver.find_element(*self._locator.check(number))
        element.click()

    def get_transferinfo(self, number):
        pass
    TODO:

    def input_amount(self, amount):
        element = self._driver.find_element(*self._locator.INPUT_AMOUNT)
        element.send_keys(amount)

    def input_client_name(self, name):
        element = self._driver.find_element(*self._locator.INPUT_CLIENT_NAME)
        element.send_keys(name)

    def click_next(self):
        element = self._driver.find_element(*self._locator.BUTTON_NEXT)
        element.click()
        return TransferConfirmPage(self._driver)


class TransferConfirmPage(BasePage):
    _locator = TransferConfirmPageLocator()

    def confirms(self):
        result = []

        element = self._driver.find_element(*self._locator.TEXT_PASSCODE_1)
        result.append(mojimoji.zen_to_han(element.text))

        element = self._driver.find_element(*self._locator.TEXT_PASSCODE_2)
        result.append(mojimoji.zen_to_han(element.text))

        element = self._driver.find_element(*self._locator.TEXT_PASSCODE_3)
        result.append(mojimoji.zen_to_han(element.text))
        return result

    def input_passcode(self, code1, code2, code3):
        element = self._driver.find_element(*self._locator.INPUT_PASSCODE_1)
        element.send_keys(code1)

        element = self._driver.find_element(*self._locator.INPUT_PASSCODE_2)
        element.send_keys(code2)

        element = self._driver.find_element(*self._locator.INPUT_PASSCODE_3)
        element.send_keys(code3)

    def click_confirm(self):
        element = self._driver.find_element(*self._locator.BUTTON_CONFIRM)
        element.click()
        return TransferCompletePage(self._driver)


class TransferCompletePage(BasePage):
    _locator = TransferCompletePageLocator()

    def click_logout(self):
        element = self._driver.find_element(*self._locator.BUTTON_LOGOUT)
        element.click()
