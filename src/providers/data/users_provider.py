import os


class UsersProvider:

    @staticmethod
    def fake_user():
        return {"login": "somenameththhghgh",
                "password": '606060604dfdf'}

    @staticmethod
    def existing_user():
        return {"login": "defunkt",
                "id": "2"}

    @staticmethod
    def existing_user_from_env():
        return {"login": os.environ.get("EXISTING_GITHUB_USER_LOGIN"),
                "id": os.environ.get("EXISTING_GITHUB_USER_ID")
                }
