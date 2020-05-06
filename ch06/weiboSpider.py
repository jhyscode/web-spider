# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 19:01
# @Author  : jhys
# @FileName: weiboSpider.py

from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
import time

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'MWeibo-Pwa': '1',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://m.weibo.cn/u/3263969254',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': '21559e',
}
def get_parge(since_id):
    params = {
        # 'type': 'uid',
        # 'value': '3263969254',
        'containerid': '1076033263969254',
        'since_id': since_id
    }
    url = base_url + urlencode(params)
    try:
        #print(url)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            #print(response.json())
            return response.json()
    except requests.ConnectionError as e:
        print('Error:',e.args)

def parse_page(json):
    if json:
        next_since_id = json.get('data').get('cardlistInfo').get('since_id')
        items = json.get('data').get('cards')
        for item in items:
            scheme = item.get('scheme')
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            weibo['item_url'] = scheme
            yield weibo

min_since_id = ''
def get_since_id():
    global min_since_id  # 在函数内部成功的修改了全局变量的数值
    top_url = 'https://m.weibo.cn/api/container/getIndex?containerid=1076033263969254'
    top_url = top_url + '&since_id=' + str(min_since_id)
    result = requests.get(top_url, headers=headers)
    json = result.json()
    min_since_id = json.get('data').get('cardlistInfo').get('since_id')
    return min_since_id

def main():
    results_all = []
    first_page_json = get_parge('')
    first_page_results = parse_page(first_page_json)
    for result in first_page_results:
        print(result)
    for i in range(12):
        time.sleep(1)
        # print('第{}页'.format(i))
        # print(get_since_id())
        json = get_parge(get_since_id())
        results = parse_page(json)
        for result in results:
            print(result)

if __name__ == '__main__':
    main()
     # json = get_parge()
     # results = parse_page(json)
     # for result in results:
     #     print(result)