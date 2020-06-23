#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Creation: 22/06/2020  20:09
@Author: liang
@File: test_py_module_settings.py
"""
import pytest

from py_settings.patch import patch_settings


def test_correct_module_settings():
    patch_settings('tests.factory.correct_settings')
    from tests.factory import correct_settings as settings
    assert settings.PY_INT == 20
    assert settings.PY_FLOAT == 20.5
    assert settings.PY_BOOL is True
    assert settings.PY_STR == 'py string'
    assert settings.PY_LIST == ['py', 'list']
    assert settings.PY_SET == {'py', 'set'}
    assert settings.PY_TUPLE == ('py', 'tuple')
    assert settings.PY_DICT == {'py': 'dict'}

    assert settings.PY_ENV_RAW is None
    assert settings.PY_ENV_DEFAULT_NO_TYPE == 'py_env_default_str'
    assert settings.PY_ENV_DEFAULT_STR == 'py_env_str'
    assert settings.PY_ENV_DEFAULT_INT == 20
    assert settings.PY_ENV_DEFAULT_FLOAT == 20.5
    assert settings.PY_ENV_DEFAULT_BOOL is True

    assert settings.CONFIG_RAW == 'config_raw'
    assert settings.CONFIG_DEFAULT_NO_TYPE == 'config_default_str'
    assert settings.CONFIG_DEFAULT_STR == 'config_default_str'
    assert settings.CONFIG_STR_INT == '20'
    assert settings.CONFIG_REAL_INT == 20
    assert settings.CONFIG_STR_FLOAT == '20.5'
    assert settings.CONFIG_REAL_FLOAT == 20.5
    assert settings.CONFIG_STR_BOOL == 'false'
    assert settings.CONFIG_REAL_BOOL is False


def test_non_declared_module_settings_failed():
    with pytest.raises(Warning) as e:
        patch_settings('tests.factory.non_declared_module_settings')

    assert 'should be declared' in str(e)


def test_invalid_section_config_settings_failed():
    with pytest.raises(Warning) as e:
        patch_settings('tests.factory.invalid_section_config_settings')
    assert 'Invalid config sections' in str(e)


def test_non_exist_module_settings_failed():
    with pytest.raises(ModuleNotFoundError):
        patch_settings('tests.factory.non_exist_module_settings')


def test_config_non_exist_settings_failed():
    with pytest.raises(Exception) as e:
        patch_settings('tests.factory.config_non_exist_settings')
    assert 'not found' in str(e)


def test_module_settings_coverage_ok():
    patch_settings('tests.factory.correct_settings', valid_envs=['default', 'dev', 'test'])
    patch_settings('tests.factory.correct_settings', api_env_key='ENV')
    patch_settings('tests.factory.correct_settings', config_file_key='__config_files__')
