# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from smtb_direct.core.locator import *


class LoginPageLocator:
    BUTTON_LOGIN = (
        By.CSSSELECTOR,
        "#l-content > div > div > div > div > div:nth-child(2) > div.mod-box-description-02__content > div.mod-button-lyt > div > div > div > a",
    )
