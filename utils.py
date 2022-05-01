import time
import base64
import hashlib

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'


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


def str_cookie_dict(cookies):
    """浏览器copy的cookies字符串，转为dict

    Args:
        cookies (_type_): _description_
    """
    cookies_list = cookies.split(';')
    datas = [cookies.strip().split('=') for cookies in cookies_list if cookies]
    result = {data[0]: data[1] for data in datas if len(data) == 2}
    return result


def get_str_md5(content: str):
    """计算字符串md5值

    Args:
        content (_type_): _description_

    Returns:
        _type_: _description_
    """
    md5hash = hashlib.md5(content.encode('utf8'))
    md5 = md5hash.hexdigest()
    return md5


def get_file_md5(file_path: str):
    """计算文件md5值

    Args:
        file_path (str): _description_
    """
    with open(file_path, 'rb') as fp:  # 模式要用'rb'
        data = fp.read()  # 一次将文件全部读入内存
    file_md5 = hashlib.md5(data).hexdigest()  # 已经是byte不用encode
    return file_md5


def get_big_file_md5(file_path: str):
    """计算大文件的MD5值，每次取4M

    Args:
        file_path (str): _description_

    Returns:
        _type_: _description_
    """
    m = hashlib.md5()  # 创建md5对象
    with open(file_path, 'rb') as fp:
        while True:
            data = fp.read(4096)  # 每次读取4MB
            if not data:
                break
            m.update(data)  # 更新md5对象
    return m.hexdigest()


if __name__ == "__main__":
    pass
