from selenium import webdriver
from smtb_direct.controller import *

CHROME_PATH = "bin\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=CHROME_PATH)

myhp = SMTBDirect(driver, config_file="config.ini")

# 1番目の振込先に1円振込
myhp.login()
myhp.get_transferinfo(11)
myhp.transfer(11, 1)
myhp.logout()
