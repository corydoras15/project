import requests
def call_api(keyword, start, display):
    url = f"https://openapi.naver.com/v1/search/blog.json?query={keyword}&start={start}&display={display}"
    res = requests.get(url, headers={"X-Naver-Client-Id":"b5rMowhxO2U7tMf58IFG", "X-Naver-Client-Secret":"UWXRw0ZusX"})

    print(res)
    r = res.json()
    return r

def get_paging_call(keyword, quantity):
    if quantity >1100:
        exit("ERROR 최대 요청 건수는 1100건 입니다.")
    repeat = quantity // 100
    result = []
    for i in range(repeat):
        start = i * 100 + 1
        if start > 1000:
            start = 1000
        print(f"{i+1}번 반복 합니다. start:{start}")
        r = call_api(keyword, start=start, display=100)
        result += r['items']
    return result

if __name__ == '__main__':
    r = get_paging_call("잠실 햄버거", 1100)