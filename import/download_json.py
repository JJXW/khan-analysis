# -*- coding: utf-8 -*-
"""
Created on Mon Jun 01 23:35:49 2015

@author: jowang
"""

import requests
import json

test = json.loads(requests.get('http://www.khanacademy.org/api/v1/playlists').text)

