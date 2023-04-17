class EnvNotFoundException(Exception):
    """
    The environment is not found.
    """

    def __init__(self, env: str) -> None:
        self.msg: str = f"The {env} is empty."

    def __str__(self) -> str:
        return self.msg
