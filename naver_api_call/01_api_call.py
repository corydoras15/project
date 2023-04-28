import requests
def call_api(keyword, start, display):
    url = f"https://openapi.naver.com/v1/search/blog.json?query={keyword}&start={start}&display={display}"
    res = requests.get(url, headers={"X-Naver-Client-Id":"b5rMowhxO2U7tMf58IFG", "X-Naver-Client-Secret":"UWXRw0ZusX"})

    print(res)
    r = res.json()
    return r

if __name__ == '__main__':
    r = call_api("잠실 맛집", 101, 10)
    for item in r['items']:
        print(item)