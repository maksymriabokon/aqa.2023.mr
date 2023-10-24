import json 
import os

class ConfigEasy:
  """Config class is responsible to storing framework's and env's configuration"""
  request_timeout = 40
  user_name = os.environ.get ('USERNAME') 
  env = os.environ.get ('AQA_ENV_MR')
  my_os= os.environ.get('OS')

config= ConfigEasy()

print(config.request_timeout)
print(config.user_name)
print(config.env)
print(config.my_os)


