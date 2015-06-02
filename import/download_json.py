# -*- coding: utf-8 -*-
"""
Created on Mon Jun 01 23:35:49 2015

@author: jowang
"""

import requests
import json
import pandas

test = json.loads(requests.get('http://www.khanacademy.org/api/v1/playlists').text)

test_data_frame=pandas.io.json.json_normalize(test)

test2 = json.loads(requests.get('http://www.khanacademy.org/api/v1/topictree').text)

test_data_frame2=pandas.io.json.json_normalize(test)

