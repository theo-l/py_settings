#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Creation: 22/06/2020  20:06
@Author: liang
@File: correct_settings.py
"""

PY_INT = 20
PY_FLOAT = 20.5
PY_BOOL = True
PY_STR = 'py string'
PY_LIST = ['py', 'list']
PY_SET = {'py', 'set'}
PY_TUPLE = ('py', 'tuple')
PY_DICT = {'py': 'dict'}

PY_ENV_RAW = '${PY_ENV_RAW}'
PY_ENV_DEFAULT_NO_TYPE = '${PY_ENV_DEFAULT_NO_TYPE:py_env_default_str}'
PY_ENV_DEFAULT_STR = '${PY_ENV_DEFAULT_STR:py_env_str<str>}'
PY_ENV_DEFAULT_INT = '${PY_ENV_DEFAULT_INT:20<int>}'
PY_ENV_DEFAULT_FLOAT = '${PY_ENV_DEFAULT_FLOAT:20.5<float>}'
PY_ENV_DEFAULT_BOOL = '${PY_ENV_DEFAULT_BOOL:true<bool>}'
PY_ENV_DEFAULT_DICT = '${PY_ENV_DEFAULT_DICT:{"name":"demo"}<dict>}'
PY_ENV_DEFAULT_LIST = '${PY_ENV_DEFAULT_LIST:1,2,3,4<list>}'
PY_ENV_DEFAULT_SET = '${PY_ENV_DEFAULT_SET:1,2,3,4<set>}'
PY_ENV_DEFAULT_TUPLE = '${PY_ENV_DEFAULT_TUPLE:1,2,3,4<tuple>}'

_config_files_ = ['config/config.ini']
CONFIG_RAW = None
CONFIG_DEFAULT_NO_TYPE = None
CONFIG_DEFAULT_STR = None
CONFIG_STR_INT = None
CONFIG_REAL_INT = None
CONFIG_STR_FLOAT = None
CONFIG_REAL_FLOAT = None
CONFIG_STR_BOOL = None
CONFIG_REAL_BOOL = None
