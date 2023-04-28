import requests
from libs.Evparser import EvOrKrparser

url = "https://www.ev.or.kr/portal/localInfo"
data = requests.get(url)

ev_parser = EvOrKrparser(data.text)
ev_parser.save_to_excel("ev_save.xlsx")
#ev_parser.parse()