#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

import collections
import requests
from config import Key

sample_url = "https://translation.googleapis.com/language/translate/v2?q={input}&target=zh-CN&key=%s" % Key['google']['translate_key']


def translate(input):
    url = sample_url.replace("{input}", input)
    res = requests.get(url)
    return res.json()['data']['translations'][0]['translatedText']


data = json.load(open('en.json'), object_pairs_hook=collections.OrderedDict)

for key, value in data.items():
    for k, v in value.items():
        if type(v) == str:
            value[k] = translate(v)
        else:
            for k1, v1 in v.items():
                v[k1] = translate(v1)
'''
for key, value in data.items():
    for k, v in value.items():
        if (type(v) == str):
            print(v)
        else :
            for k1, v1 in v.items():
                print(v1)
'''

with open('zh.json', 'w', encoding='utf-8') as out:
    res = json.dump(data, out, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
