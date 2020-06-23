# py_settings
A simple explicit module level settings with env and file configuration

## Description
 Nowadays, we have a lot of libs to help us configure our project, like dotenv, Django, dynaconf, etc. 
 But I prefer to follow the ZEN of python *explicit is better than implicit*. 

 I created this project to make project setting more explicit which will help us know better about all
 our projection configuration options during configuration period, and also make the IDE more friendly
 during the programming period. 

## Quick tour

If we have a project like the following structure:

<pre>
project/
    |
    |
    |_main.py
    |
    |_settings.py
    |
    |_config.ini

</pre>

In our `settings.py` we can specify the following configuration options:

- Raw python value/object option value, which will keep their origin value: `PY_INT = 20`
- Environment values: `PY_ENV_VALUE=${PY_ENV_VALUE:default_env_value<converter>}`
    - Environment value without default value, which will be `None` if environment variable not exist
    - Environment value with default, but no converter. which will have the default value with string type
    - Environment value with default and convert: the value will be converted to the right datatype, will raise Exception if can not be converted to the right data type
- Configuration file support( `.ini`), the following parts should be noticed:
    - All configuration options in the configure file should be declared in `settings.py` with uppercase format
    - It's better only keep the environment related plain text configuration, no environment(even this is supported)
    - The sections should follow: ['default', 'test', 'development', 'homolog', 'staging', 'production']. Of course you can cusomize these section during the initiate process

 For example, we want to configure a mongo database connection for our project, in our `settings.py`, should be like:
 
 ```python
API_ENV='${API_ENV:dev}'

MONGO_DB_URI='${MONGO_DB_URI:mongodb://localhost:27017}' # sensible environment dependent data 

COLLECTION_NAME = 'collections' #none environment dependent plain text data 

_config_files_=['./config.ini']

MONGO_DB_NAME=None # environment dependent plain text data we can save in config.ini(reduce environment variable count)  

```

in our `config.ini`, we can save some non sensible environment dependent data, to avoid too much environment variable
```toml
[default]
MONGO_DB_NAME = dev_demoDB

[test]
MONGO_DB_NAME = test_demoDB

[staging]
MONGO_DB_NAME = staging_demoDB

[production]
MONGO_DB_NAME = demoDB

```

Then, in our `main.py` we can use these configurations as following:

```python
from py_settings.patch import patch_settings
patch_settings('project.settings') # **NOTE**, this call must be called before import the real setting module
from example import settings

def main():
    print('settings')
    


```




