from selenium import webdriver
from core.controller import *

CHROME_PATH = "bin\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=CHROME_PATH)

myhp = SMTBDirect(driver, config_file="config.ini")

myhp.login()
myhp.transfer(11, 1)
