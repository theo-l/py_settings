#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Creation: 22/06/2020  22:08
@Author: liang
@File: settings.py
"""

COLLECTION_NAME = 'demos'  # non-environment dependent plain text data

API_ENV = '${API_ENV:dev}'
# environment dependent sensible data
MONGO_DB_URL = '${MONGO_DB_URL:mongodb://localhost:27017}'

TYPE_VAR = '${TYPE_VAR:125<int>}'
DICT_VAR = '${DICT_VAR:{"name":"demo"}<dict>}'
LIST_VAR = '${LIST_VAR:a,b,c<list>}'
SET_VAR = '${SET_VAR:d,e,f<set>}'
TUPLE_VAR = '${TUPLE_VAR:g,h,i<tuple>}'

_config_files_ = ['config.ini']  # environment dependent plain text data
MONGO_DB_NAME = None
