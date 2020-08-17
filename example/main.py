#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Creation: 22/06/2020  22:08
@Author: liang
@File: main.py
"""
from py_settings.patch import patch_settings

patch_settings('example.settings')
from example import settings  # noqa


def main():
    print(settings.API_ENV)
    print(settings.MONGO_DB_URL)
    print(settings.MONGO_DB_NAME)
    print(settings.COLLECTION_NAME)
    print(settings.TYPE_VAR)
    print(settings.DICT_VAR, type(settings.DICT_VAR))
    print(settings.LIST_VAR, type(settings.LIST_VAR))
    print(settings.SET_VAR, type(settings.SET_VAR))
    print(settings.TUPLE_VAR, type(settings.TUPLE_VAR))


if __name__ == '__main__':
    main()
