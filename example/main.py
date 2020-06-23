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


if __name__ == '__main__':
    main()
