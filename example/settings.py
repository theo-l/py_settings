#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Creation: 22/06/2020  22:08
@Author: liang
@File: settings.py
"""

API_ENV = '${API_ENV:dev}'
MONGO_DB_URL = '${MONGO_DB_URL:mongodb://localhost:27017}'  # environment dependent sensible data
COLLECTION_NAME = 'demos'  # non-environment dependent plain text data

_config_files_ = ['./config.ini']  # environment dependent plain text data
MONGO_DB_NAME = None
