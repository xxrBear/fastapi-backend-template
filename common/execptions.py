class BusinessException(Exception):
    """业务异常"""

    def __init__(self, name: str):
        self.name = name
