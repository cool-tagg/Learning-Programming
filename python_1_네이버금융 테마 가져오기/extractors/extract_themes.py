from requests import get
from bs4 import BeautifulSoup

def get_page_count(): # BeautifulSoup의 함수로 html.parser을 가져와야함
        link_base = "https://finance.naver.com/sise/theme.naver"
        response = get(link_base)
        soup = BeautifulSoup(response.text, 'html.parser')
        td_class_pgRR = soup.find('td', class_='pgRR')
        anchor = td_class_pgRR.find('a')
        link = anchor['href']
        return link[-1]     # 마지막 페이지의 url(string)의 가장 뒤에 page number가 적혀있음
def get_themes_onePage(num_page):
        if num_page == 1:
            link_base = "https://finance.naver.com/sise/theme.naver"
        else:
            link_base = f"https://finance.naver.com/sise/theme.naver?&page={num_page}"
        result = []
        
        response = get(link_base)
        soup = BeautifulSoup(response.text, "html.parser")
        td_col_type1 = soup.find_all('td', class_="col_type1")

        i = (num_page -  1) * 40
        for td in td_col_type1:
            i += 1
            anchor = td.find('a')
            name = anchor.string  # Html tag 안의 content(내용)을 보여준다.
            link = f"https://finance.naver.com/{anchor['href']}"
            theme_name_ = {
                'page' : num_page,
                'order': i,
                'name' : name.string.replace(',', ' '),
                'link' : link
            }
            
            result.append(theme_name_)
        return result
def get_themes_allPage():
    link_base = "https://finance.naver.com/sise/theme.naver"
    response = get(link_base)
    soup = BeautifulSoup(response.text, "html.parser")

    links_page = []
    links_page.append(link_base)

    num_lastPage = int(get_page_count())

    for i in range(num_lastPage - 1):
        i += 2
        page_link = "https://finance.naver.com/sise/theme.naver?&page=" + str(i)
        links_page.append(page_link)
        


    result = []
    for i in range(num_lastPage):
        themes = get_themes_onePage(i)
        result += themes
    
    
    return result


