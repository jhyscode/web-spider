import requests
def get_response(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    r = requests.get(url,headers=headers)
    print(r.text)

if __name__ == '__main__':
    url = 'https://www.zhihu.com/people/jiang-hu-yin-shi/following?page=1'
    get_response(url)