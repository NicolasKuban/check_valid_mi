import requests
from datetime import date, datetime
from time import sleep

URL = 'https://fgis.gost.ru/fundmetrology/eapi/vri?'
DATE_URL = '%Y-%m-%d'
DATE_XLS = '%d.%m.%Y'

def get_url(item):
    options = (
        f'mi_number={item.number}',
        f'mit_number={item.fif}',
        f'verification_date_start={item.date_dispatch.strftime(DATE_URL)}',
    )
    return URL + '&'.join(options)

def set_requests(url):
    try:
        response = requests.get(url).json()['result']['items']
    except:
        print('Увеличено время ожидания ответа')
        sleep(5.0)
        response =requests.get(url).json()['result']['items']
    sleep(0.5)
    return response

def get_response(item):
    url = get_url(item)
    response = set_requests(url)
    return response

if __name__ == '__main__':
    from collections import namedtuple
    Mi = namedtuple('Mi', 'number fif date_dispatch')
    # item = Mi('6152', '43761-10', datetime.strptime('16.07.2024', DATE_XLS))
    item = Mi('35', '35279-07', datetime.strptime('16.01.2024', DATE_XLS))
    print(item)
    url = get_url(item)+'&rows=100'
    print(url)
    response = get_response(url)
    print(response)
    print('============', len(response))