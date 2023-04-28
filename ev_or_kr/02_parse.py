from bs4 import BeautifulSoup

f = open("local_info.html")
page_string = f.read()
bsobj = BeautifulSoup(page_string, "html.parser")
table = bsobj.find("table", {"class":"table_02_2_1"})
trs = table.find("tbody").find_all("tr")
tr = trs[0]

ths = tr.find_all("th")
tds = tr.find_all("td")

sido = ths[0].text
region = ths[1].text

replace_brackets = lambda x: x.replace("(", "").replace(")", "").split(" ")[1:]

민간공고대수 = replace_brackets(tds[2].text)
접수대수 = replace_brackets(tds[3].text)
출고대수 = replace_brackets(tds[4].text)
출고잔여대수 = replace_brackets(tds[5].text)

row = {"sido":sido, "region":region, "sep1":"민간공고대수", "sep2":"우선순위", "value":780}
row2 = {"sido":sido, "region":region, "sep1":"민간공고대수", "sep2":"법인,기관", "value":0}
row3 = {"sido":sido, "region":region, "sep1":"민간공고대수", "sep2":"택시", "value":1500}
row4  = {"sido":sido, "region":region, "sep1":"민간공고대수", "sep2":"우선비대상", "value":4020 }
print(row)
