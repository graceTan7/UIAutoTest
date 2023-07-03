# -*- coding: utf-8 -*-
# @Author  : gracetan
from TestDatas import Comm_Datas

success_data = {"email": Comm_Datas.email, "passwd": Comm_Datas.pwd}
wrong_datas = [{"email": " ", "passwd": "eventx", "check": "Email is required."},
               {"email": "eventx@eventx.io", "passwd": " ", "check": "Password is required."}]
fail_datas = [{"email": "eventx@", "passwd": "eventx", "check": "Invalid email or password"},
              {"email": "eventx@eventx.io", "passwd": "11111111", "check": "Invalid email or password"}]