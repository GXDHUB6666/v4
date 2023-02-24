from selenium.webdriver.common.by import By
# 登录链接
login_link = By.PARTIAL_LINK_TEXT,'登录'
login_username = By.NAME,'accounts'
login_pwd = By.NAME,'pwd'
login_btn = By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button'
login_err_btn = By.CLASS_NAME,'prompt-msg'
login_quit = By.PARTIAL_LINK_TEXT,'退出'
login_url = 'http://shop-xo.hctestedu.com/'