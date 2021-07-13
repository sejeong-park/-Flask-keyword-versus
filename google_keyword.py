import requests
from bs4 import BeautifulSoup

def get_keyword_number(keyword):
    #keyword="나루토"
    url = "https://www.google.com/search?q={}".format(keyword)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

    # 웹 요청
    res = requests.get(url, headers=headers)
    #print(res.text)


    # 구문 분석 - 파싱 (soup라고 할 것)
    soup = BeautifulSoup(res.text, 'lxml')
    #print(soup)

    # 원하는 것 추출
    number = soup.select_one('#result-stats').text
    print(number)
    #정리
    #print(number[number.find('약')+2:number.rfind('개')].replace(',','')) #얖에서 나올것부터 찾고 뒤에 나올것 찾고, 글자 빼고 다 빼줌//replace는 컴마 없애기

    number=int(number[number.find('약')+2:number.rfind('개')].replace(',',''))
    #print(number)

    return number

#테스트 코드
if __name__=="__main__":
    pass





