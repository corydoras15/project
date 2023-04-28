import os.path
import requests
from urllib.request import Request, urlopen

class NaverSearchApi():

    api_url = "https://openapi.naver.com/v1/search/blog.json"

    def call_api(self, keyword, start=1, display=10):
        url = f"{self.api_url}?query={keyword}&start={start}&display={display}"
        res = requests.get(url, headers={"X-Naver-Client-Id": "b5rMowhxO2U7tMf58IFG", "X-Naver-Client-Secret": "UWXRw0ZusX"})

        print(res)
        r = res.json()
        return r

    def get_paging_call(self, keyword, quantity):
        if quantity > 1100:
            exit("ERROR 최대 요청 건수는 1100건 입니다.")
        repeat = quantity // 100
        display = 100
        if quantity < 100:
            display = quantity
            repeat =1
        result = []
        for i in range(repeat):
            start = i * 100 + 1
            if start > 1000:
                start = 1000
            print(f"{i + 1}번 반복 합니다. start:{start}")
            r = self.call_api(keyword, start=start, display=display)
            result += r['items']
        return result

    def save_images(self, path, r):
        if not os.path.exists(path):
            os.mkdir(path)

        cnt = 0
        for img in r:
            try:
                image_url = img['link']
                image_byte = Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
                f = open(f'{path}/{cnt}.jpg', 'wb')
                f.write(urlopen(image_byte).read())
                f.close()
            except Exception as e:
                print(e)
            cnt += 1

    def blog(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/blog.json"
        return self.get_paging_call(keyword, quantity)

    def news(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/news.json"
        return self.get_paging_call(keyword, quantity)

    def webkr(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/webkr.json"
        return self.get_paging_call(keyword, quantity)

    def image(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/image"
        return self.get_paging_call(keyword, quantity)

if __name__ == '__main__':
    naver_search_api = NaverSearchApi()
    keyword = "송파역"
    r = naver_search_api.image(keyword, 100)
    print(len(r))
    naver_search_api.save_images(keyword, r)