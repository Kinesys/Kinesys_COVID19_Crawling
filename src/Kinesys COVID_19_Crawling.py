#Kinesys COVID_19_Crawling.py
import pandas as pd 
import urllib,request as urllib

site_url = "https://ncov.mohw.go.kr/bdBoardList_Real.do" #크롤링을 진행할 사이트 주소

openner = urllib.build_opener()

openner.addheaders = [('User_Agent', 'Mozilla/5.0')]

params = {
    'brdId' : 1
    'brdGubun' : 14,
}

