from selenium import webdriver
from smtb_direct.controller import *

CHROME_PATH = "bin\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=CHROME_PATH)

myhp = SMTBDirect(driver, config_file="config.ini")

myhp.login()

# 口座情報を表示
bl = myhp.get_balance()
print(bl)

# 振込先を全部表示
res = myhp.get_transferinfo()
if res:
    for r in res:
        print(r)

# 2番目の振込先に1円振込
myhp.transfer(2, 1)
myhp.logout()
