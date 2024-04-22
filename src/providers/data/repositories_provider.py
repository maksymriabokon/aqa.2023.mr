class ReposiroriesProvider:

    @staticmethod
    def existing_repository():
        return {"total count": 1,
                "name": "become-qa-auto"}

    @staticmethod
    def non_existing_repository():
        return {"total count": 0,
                "name": "fgfgnhdfdgfhjhgkghf"}
