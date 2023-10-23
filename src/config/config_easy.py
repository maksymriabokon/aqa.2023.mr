import os

class ConfigEasy:
  """Config class is responsible to storing framework's and env's configuration"""
  request_timeout = 40
  user_name = os.environ.get ('USERNAME') # or get it from elsewhere
  env = os.environ.get ('AQA_ENV_MR')
  home=os.environ.get ('HOME')
 

config= ConfigEasy()

print(config.request_timeout)
print(config.user_name)
print(config.env)
print(config.home)