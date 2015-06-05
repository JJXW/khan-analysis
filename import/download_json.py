# -*- coding: utf-8 -*-
"""
Created on Mon Jun 01 23:35:49 2015

@author: jowang
"""

import requests
import json
import pandas


khan_tree_request = requests.get('http://www.khanacademy.org/api/v1/topictree')

khan_tree_json = json.loads(khan_tree_request.text)

khan_tree_math_df=pandas.io.json.json_normalize(khan_tree_json['children'][1]['children'])

# Description of first child layer gives the topic

khan_tree_json['children'][0]['description'] # No description, but I'm guessing it's misc Khan videos
khan_tree_json['children'][1]['description'] # Math!
khan_tree_json['children'][2]['description'] # Description is missing, but it is Natural Science
khan_tree_json['children'][3]['description'] # Econ / Finance

# Description of second child layer describes video

khan_tree_json['children'][0]['children'][3]['description'] # LeBrick
khan_tree_json['children'][1]['children'][10]['description'] # Algebra 
khan_tree_json['children'][2]['children'][2]['description'] # Chemistry
