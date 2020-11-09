#Kinesys COVID_19
import pandas as pd 
import urllib,request as urllib

site_url = "https://ncov.mohw.go.kr/bdBoardList_Real.do" #크롤링을 진행할 사이트 주소

params = {
    'brdId' : 1
    'brdGubun' : 14,
}

response = request.get(page_url, params=params)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

html = str(soup.select_one(".data_table.mgt16"))

