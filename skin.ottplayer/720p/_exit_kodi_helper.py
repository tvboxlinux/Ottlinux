#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# clean LibreELEC KODI restart
os.system("systemctl restart kodi")

# more aggressive
#os.system("killall -HUP kodi.bin")
