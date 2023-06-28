# -*- coding: utf-8 -*-
# @Author  : gracetan

success_data = {"email": "eventx@eventx.io", "passwd": "eventx"}
wrong_datas = [{"email": " ", "passwd": "eventx", "check": "Email is required."},
               {"email": "eventx@eventx.io", "passwd": " ", "check": "Password is required."}]
fail_datas = [{"email": "eventx@", "passwd": "eventx", "check": "Invalid email or password"},
              {"email": "eventx@eventx.io", "passwd": "11111111", "check": "Invalid email or password"}]