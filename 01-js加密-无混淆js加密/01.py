import requests
from utils import str_cookie_dict, get_timestamp, btoa, get_str_md5, ua
from lxml import etree
from loguru import logger

sessionid = 'sessionid = 自行拷贝'
headers = {
    'user-agent': ua,
    'no-alert': 'true',
    'referer': 'https://www.python-spider.com/challenge/1',
    'x-requested-with': 'XMLHttpRequest'
}


def get_timestamp_safe():
    # var a = '9622';
    # var timestamp = String(Date.parse(new Date()) / 1000);
    # var tokens = hex_md5(window.btoa(a + timestamp));
    a = '9622'
    timestamp = str(get_timestamp() // 1000)
    safe = get_str_md5(btoa(a + timestamp))
    return {'timestamp': timestamp, 'safe': safe}


def get_data():
    count = 0
    keyword = '招'
    for page in range(1, 85 + 1):
        logger.info(f'正在进行第{page}页')
        url = f'https://www.python-spider.com/challenge/api/json?page={page}&count=14'
        headers.update(get_timestamp_safe())
        resp = requests.get(url=url, headers=headers, cookies=str_cookie_dict(sessionid))
        result = resp.json()
        infos = result.get('infos', [{}])
        titles = [info.get('message', '') for info in infos]
        for title in titles:
            if keyword in title:
                count += 1
        logger.info(f'count:{count}')
    return count


def main():
    count = get_data()
    logger.info(f'answer:{count}')


if __name__ == "__main__":
    main()
