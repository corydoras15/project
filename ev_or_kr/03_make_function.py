from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

def parse_tr(tr):
    ths = tr.find_all("th")
    tds = tr.find_all("td")

    sido = ths[0].text
    region = ths[1].text

    replace_brackets = lambda x: x.replace("(", "").replace(")", "").split(" ")[1:]
    form = lambda a, b, c, d, e: {"sido": a, "region": b, "sep1": c, "sep2": d, "value": e}
    민간공고대수 = replace_brackets(tds[2].text)
    접수대수 = replace_brackets(tds[3].text)
    출고대수 = replace_brackets(tds[4].text)
    출고잔여대수 = replace_brackets(tds[5].text)

    row = {"sido": sido, "region": region, "sep1": "민간공고대수", "sep2": "우선순위", "value": 780}
    row2 = {"sido": sido, "region": region, "sep1": "민간공고대수", "sep2": "법인,기관", "value": 0}
    row3 = {"sido": sido, "region": region, "sep1": "민간공고대수", "sep2": "택시", "value": 1500}
    row4 = {"sido": sido, "region": region, "sep1": "민간공고대수", "sep2": "우선비대상", "value": 4020}

    l = [
        form(sido, region, "민간공고대수", "우선순위", int(민간공고대수[0])),
        form(sido, region, "민간공고대수", "법인,기관", int(민간공고대수[1])),
        form(sido, region, "민간공고대수", "택시", int(민간공고대수[2])),
        form(sido, region, "민간공고대수", "우선비대상", int(민간공고대수[3])),
        form(sido, region, "접수대수", "우선순위", int(접수대수[0])),
        form(sido, region, "접수대수", "법인,기관", int(접수대수[1])),
        form(sido, region, "접수대수", "택시", int(접수대수[2])),
        form(sido, region, "접수대수", "우선비대상", int(접수대수[3])),
        form(sido, region, "출고대수", "우선순위", int(출고대수[0])),
        form(sido, region, "출고대수", "법인,기관", int(출고대수[1])),
        form(sido, region, "출고대수", "택시", int(출고대수[2])),
        form(sido, region, "출고대수", "우선비대상", int(출고대수[3])),
        form(sido, region, "출고잔여대수", "우선순위", int(출고잔여대수[0])),
        form(sido, region, "출고잔여대수", "법인,기관", int(출고잔여대수[1])),
        form(sido, region, "출고잔여대수", "택시", int(출고잔여대수[2])),
        form(sido, region, "출고잔여대수", "우선비대상", int(출고잔여대수[3]))
    ]
    return (l)

if __name__ == '__main__':
    f = open("local_info.html")
    page_string = f.read()
    bsobj = BeautifulSoup(page_string, "html.parser")
    table = bsobj.find("table", {"class": "table_02_2_1"})
    trs = table.find("tbody").find_all("tr")
    tr = trs[0]

    m = []
    for tr in trs:
        try:
            row = parse_tr(tr)
            m += row
        except Exception as e:
            print(e)

    df = pd.DataFrame(m)
    print(df)
    df.to_excel("all_sido.xlsx")