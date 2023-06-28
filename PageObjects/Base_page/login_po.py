# -*-encoding:utf-8-*-
# @Author  : gracetan
''' login '''

from WebCommon.BasePage import BasePageObjects
from PageLocators.Base_loc import login_loc


class Login(BasePageObjects):

    def email_login(self, email, pwd):
        self.input_text(login_loc.loc_Email, email)
        self.input_text(login_loc.loc_Pwd, pwd)
        self.click_element(login_loc.log_LogIn, "login button")

    # 获取表单区域的错误信息
    def get_error_msg_from_loginForm(self):
        msg = None
        try:
            msg = self.get_element_text(login_loc.error_email_required, "Email is required.")
        except:
            msg = self.get_element_text(login_loc.error_pwd_required, "Password is required.")
        finally:
            return msg

    def get_error_msg_popup(self):
        return self.get_element_text(login_loc.error_popup, "Invalid email or password")

    def forgot_password(self):
        pass

    def sign_up(self):
        pass
