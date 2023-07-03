# -*- coding: utf-8 -*-
# @Author  : gracetan
import os

email = os.getenv('USERNAME')
pwd = os.getenv('PASSWORD')

event_url = f"/events/{os.getenv('EVENT_ID')}"
check_in_url = '/physical'
portal_base_url = os.getenv('PORTAL_BASE_URL')
