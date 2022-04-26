import time
import base64


def get_timestamp():
    """获取时间戳（ms，13位）

    Returns:
        _type_: _description_
    """
    return int(time.time() * 1000)


def btoa(data: str):
    """计算base64编码值

    Args:
        data (str): _description_

    Returns:
        _type_: _description_
    """
    return base64.b64encode(data.encode()).decode()


if __name__ == "__main__":
    pass
