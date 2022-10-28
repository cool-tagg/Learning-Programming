from email import header
from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver


def encode_kr(args):
    encode = str(args.encode('EUC-KR'))
    encode = encode.replace("\\x", "%")
    encode = encode[2 : -1:]
    return encode

print("------------------------")
print("start")
print("------------------------\n")




url_FinanceNaver = "https://finance.naver.com/search/search.naver?query="
query = "삼성전자" # input("검색할 주식 명을 입력하시오: ")
query_encode = encode_kr(query)
url_search = f"https://finance.naver.com/search/search.naver?query={query_encode}"


"""
web page에서 Source 가져오기
Selenium을 활용
"""

response = get(url_search, headers=headers)











"""
1. td 태그에 'tit'클래스를 가진 요소를 찾어오기
2. 그 안에 a 태그의 string을 가져오기
"""
# tag_td_tit = html_parser.find_all('td', class_='tit')
# print(tag_td_tit)


print("\n------------------------")
print("Done")
print("------------------------")
