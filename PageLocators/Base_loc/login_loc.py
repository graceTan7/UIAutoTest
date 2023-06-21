# -*-encoding:utf-8-*-
# @Author  : gracetan
# @Time    : 2020/7/10 11:02
# @Introduction：login page loc


from selenium.webdriver.common.by import By

# 登陆系统使用按钮loc
loc_Email = (By.XPATH, '//input[@id="email"]')  # input email
loc_Pwd = (By.XPATH, '//input[@id="password"]')  # input password
log_LogIn = (By.XPATH, '//button[@type="submit"]')  # Log In button

# error loc
error_email_required = (By.XPATH, '//p[@id="email-helper-text"]')  # Email is required.
error_pwd_required = (By.XPATH, '//p[@id="password-helper-text"]')  # Password is required.
error_popup = (By.XPATH, '//div[@id="notistack-snackbar"]')  # Invalid email or password