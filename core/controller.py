# -*- coding: utf-8 -*-
from core.page import *
import configparser


class SMTBDirect:
    _url = "https://direct.smtb.jp/ap1/ib/login.do"

    def __init__(self, driver, config_file=None):
        self._driver = driver
        self._driver.get(self._url)

        self.current_page = LoginPage(self._driver)

        if config_file:
            self.config = configparser.ConfigParser()
            self.config.read(config_file)

    def login(self):

        # self._driver.get("https://direct.smtb.jp/ap1/ib/login.do")

        self.current_page.input_member()
        self.current_page.input_password()
        self.current_page = self.current_page.click_login()

    def transfer(self, number: int, amount: int, name=None):

        if isinstance(self.current_page, MenuPage):

            self.current_page = self.current_page.click_transaction()

            self.current_page = self.current_page.click_transfer()

            self.current_page.select_check(number)
            self.current_page.input_amount(amount)
            if name:
                self.current_page.input_client_name(name)

            self.current_page = self.current_page.click_next()

            c = self.current_page.confirms()
            print(c)
