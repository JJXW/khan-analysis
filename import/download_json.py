# -*- coding: utf-8 -*-
"""
Created on Mon Jun 01 23:35:49 2015

@author: jowang
"""

import requests
import json
import pandas

data_export = 'C:/Users/Jonathan/Dropbox/Coding Projects/Khan Visualization/data/raw/'

khan_tree_request = requests.get('http://www.khanacademy.org/api/v1/topictree')
khan_tree_json = json.loads(khan_tree_request.text)

# Description of first child layer gives the topic

khan_tree_json['children'][0]['description'] # No description, but I'm guessing it's misc Khan videos
khan_tree_json['children'][1]['description'] # Math!
khan_tree_json['children'][2]['description'] # Description is missing, but it is Natural Science
khan_tree_json['children'][3]['description'] # Econ / Finance

# Description of second child layer describes subject subcategory.

khan_tree_json['children'][0]['children'][3]['description'] # LeBrick
khan_tree_json['children'][1]['children'][1]['description'] # Algebra 
khan_tree_json['children'][2]['children'][2]['description'] # Chemistry


khan_tree_df = pandas.DataFrame()

def extractDFJson(json, df):
     for i in range(len(json)):
         if 'children' in json[i]:
             json_child = json[i]['children']
             df = extractDFJson(json_child, df)
         else:
             df = df.append(pandas.io.json.json_normalize(json[i]))
     print len(df)
     return df

    
test_extract = extractDFJson(khan_tree_json['children'], khan_tree_df)

test_extract = test_extract.encode('utf-8')
test_extract2 = test_extract.set_index(pandas.Series(range(len(test_extract))))

test_extract2.to_csv(data_export+'khan_video_raw.csv', encoding='utf-8')