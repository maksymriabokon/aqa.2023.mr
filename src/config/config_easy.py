import os


class Config:
    base_url_api = os.environ.get("BASE_URL_API", 'https://api.github.com')
    base_url_ui = os.environ.get("BASE_URL_UI", 'https://github.com')
