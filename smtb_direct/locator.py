# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class LoginPageLocator:
    INPUT_MEMBER = (
        By.CSS_SELECTOR,
        "#content-main > tbody > tr > td > table.data-table2 > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td:nth-child(1) > span > input",
    )
    INPUT_PASSWORD = (
        By.CSS_SELECTOR,
        "#content-main > tbody > tr > td > table.data-table2 > tbody > tr:nth-child(3) > td > table > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(1) > span > input",
    )

    BUTTON_LOGIN = (
        By.CSS_SELECTOR,
        "#btn-bottom > tbody > tr > td:nth-child(3) > span > input[type=button]",
    )


class MenuPageLocator:
    BUTTON_LOGOUT = (
        By.CSS_SELECTOR,
        "#masthead-1 > tbody > tr > td.bg-logout > form > table > tbody > tr:nth-child(2) > td > a > img",
    )

    BUTTON_TRANSACTION = (
        By.CSS_SELECTOR,
        "#navi > tbody > tr > td > table > tbody > tr > td:nth-child(3) > form > a > img",
    )


class TransactionPageLocator:
    BUTTON_TRANSFER = (
        By.CSS_SELECTOR,
        "#content-main > tbody > tr > td:nth-child(2) > div.mcp-bk-hutuuu > table.data-table1 > tbody > tr:nth-child(3) > td.data-table1-td3.mcp-mtx-hutuuu-tetuzuki > table > tbody > tr:nth-child(5) > td > span > input[type=button]",
    )


class TransferPageLocator:
    def check(self, number):
        i = number + 2
        return (
            By.CSS_SELECTOR,
            f"#hurikomisaki_jizen > table > tbody > tr:nth-child({i}) > td.data-table1-td1 > input[type=radio]",
        )

    def bank_name(self, number):
        i = number + 2
        return (
            By.CSS_SELECTOR,
            f"#hurikomisaki_jizen > table > tbody > tr:nth-child({i}) > td:nth-child(2)",
        )

    def branch_name(self, number):
        i = number + 2
        return (
            By.CSS_SELECTOR,
            f"#hurikomisaki_jizen > table > tbody > tr:nth-child({i}) > td:nth-child(3)",
        )

    def account_type(self, number):
        i = number + 2
        return (
            By.CSS_SELECTOR,
            f"#hurikomisaki_jizen > table > tbody > tr:nth-child({i}) > td:nth-child(4)",
        )

    def account_number(self, number):
        i = number + 2
        return (
            By.CSS_SELECTOR,
            f"#hurikomisaki_jizen > table > tbody > tr:nth-child({i}) > td:nth-child(5)",
        )

    def account_name(self, number):
        i = number + 2
        return (
            By.CSS_SELECTOR,
            f"#hurikomisaki_jizen > table > tbody > tr:nth-child({i}) > td:nth-child(6)",
        )

    INPUT_AMOUNT = (
        By.CSS_SELECTOR,
        "#content-main > tbody > tr > td:nth-child(2) > table:nth-child(12) > tbody > tr:nth-child(3) > td > table > tbody > tr > td > span > input",
    )
    INPUT_CLIENT_NAME = (
        By.CSS_SELECTOR,
        "#content-main > tbody > tr > td:nth-child(2) > table:nth-child(12) > tbody > tr:nth-child(5) > td > input",
    )
    BUTTON_NEXT = (
        By.CSS_SELECTOR,
        "#btn-bottom > tbody > tr > td:nth-child(3) > span > input[type=button]",
    )


class TransferConfirmPageLocator:
    TEXT_PASSCODE_1 = (
        By.CSS_SELECTOR,
        "#content-main > tbody > tr > td:nth-child(2) > table.data-table1 > tbody > tr:nth-child(3) > td.data-table2-td3 > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(1) > span > nobr",
    )
    TEXT_PASSCODE_2 = (
        By.CSS_SELECTOR,
        "#content-main > tbody > tr > td:nth-child(2) > table.data-table1 > tbody > tr:nth-child(3) > td.data-table2-td3 > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(3) > span > nobr",
    )
    TEXT_PASSCODE_3 = (
        By.CSS_SELECTOR,
        "#content-main > tbody > tr > td:nth-child(2) > table.data-table1 > tbody > tr:nth-child(3) > td.data-table2-td3 > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(5) > span > nobr",
    )

    INPUT_PASSCODE_1 = (
        By.CSS_SELECTOR,
        "#content-main > tbody > tr > td:nth-child(2) > table.data-table1 > tbody > tr:nth-child(3) > td.data-table2-td3 > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(1) > span > input",
    )
    INPUT_PASSCODE_2 = (
        By.CSS_SELECTOR,
        "#content-main > tbody > tr > td:nth-child(2) > table.data-table1 > tbody > tr:nth-child(3) > td.data-table2-td3 > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(3) > span > input",
    )
    INPUT_PASSCODE_3 = (
        By.CSS_SELECTOR,
        "#content-main > tbody > tr > td:nth-child(2) > table.data-table1 > tbody > tr:nth-child(3) > td.data-table2-td3 > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(5) > span > input",
    )
    BUTTON_CONFIRM = (
        By.CSS_SELECTOR,
        "#btn-bottom > tbody > tr > td:nth-child(3) > span > input[type=button]",
    )


class TransferCompletePageLocator:
    BUTTON_LOGOUT = (
        By.CSS_SELECTOR,
        "#masthead-1 > tbody > tr > td.bg-logout > form > table > tbody > tr:nth-child(2) > td > a > img",
    )
