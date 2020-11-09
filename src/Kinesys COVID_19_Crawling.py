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

df = pd.read_html(html)[0]

df.columns = ['지역', '국가', '도시', '격리중', '환자발생수(사망)']

df2 = df['환자발생수(사망)'].str.extract(r'([\d.]+[ㄱ-힣\s\(\)]+[\d,]*')

df = df.drop('환자발생수(사망)', axis = 1)

df['환자발생수'] = df2[0].str.replace(',', '').apply(lambda s: s and int(s))

df['환자사망수'] = df2[1].str.replace(',', '').apply(lambda s: s and int(s) or 0)


print(df.shape)
print(df.head())

#파일 저장
df.to_word("코로나.docx")
df.to_hancom("코로나.hwp")
df.to_csv("코로나.csv")
df.to_excel("코로나.xlsx")
