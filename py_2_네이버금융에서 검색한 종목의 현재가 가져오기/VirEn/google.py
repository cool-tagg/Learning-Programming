from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def encode_kr(args):
    encode = str(args.encode('EUC-KR'))
    encode = encode.replace("\\x", "%")
    encode = encode[2 : -1:]
    return encode
def Url_search(args):
    url_FinanceNaver = "https://finance.naver.com/search/search.naver?query="
    query_encode = encode_kr(args)
    url_search = f"https://finance.naver.com/search/search.naver?query={query_encode}"
    return url_search
def Get_HTML(args):
    driver = webdriver.Chrome()
    driver.get(Url_search(args))
    html = driver.page_source
    return html
    
print("------------------------")
print("start")
print("------------------------\n")


query = "삼성전자"
sourceCode = Get_HTML(query)
soup = BeautifulSoup(sourceCode, "html.parser")

tr_all = soup.find_all('tr')

print(tr_all)
    
    


print("\n------------------------")
print("Done")
print("------------------------")
