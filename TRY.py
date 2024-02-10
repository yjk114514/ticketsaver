import requests
from bs4 import BeautifulSoup

headers = {
 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
 'accept-language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
 'accept-encoding':'gzip, deflate, br',
 'referer':'https://gpoticket.globalinterpark.com/Global/Play/Book/BookSeat.asp?GoodsCode=24000291&PlaceCode=24000014&OnlyDeliver=68004&DBDay=12&ExpressDelyDay=0&GroupName=2024+Whee+In+1ST+CONCERT+%3A+WHEE+IN+THE+MOOD&PlaceName=%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%80%98%EC%96%B4+%EB%A7%88%EC%8A%A4%ED%84%B0%EC%B9%B4%EB%93%9C%ED%99%80&TmgsOrNot=D2006&LocOfImage=24000014.gif&Tiki=N&KindOfGoods=01003&GlobalSportsYN=N&isSeatCntView=N&LanguageType=G2001&MemBizCode=10965&BizCode=10965&PlayDate=20240224&PlaySeq=001&SessionId=30211BAC2F7045B6B692D31BD31B89D4&BizMemberCode=T30079727&BizMemberFlag=&GoodsBizCode=35736&WynsCode=&WynsGateID=&PageCV=',#会话不同
 'upgrade-insecure-requests':'1',
 'sec-fetch-dest':'iframe',
 'sec-fetch-mode':'navigate',
 'sec-fetch-site':'same-origin',
 'sec-fetch-user':'?1',
 'te':'trailers',
 'cookie':'_ga_BEN1B7STVY=GS1.1.1706890191.12.1.1706891552.0.0.0; _ga=GA1.2.925805744.1706529252; _fbp=fb.1.1706529254918.749465469; _ga_4SKTL7E8Q8=GS1.1.1706637275.1.0.1706637286.49.0.0; ab.storage.sessionId.cd97b079-ff05-4967-873a-324050c2a198=%7B%22g%22%3A%22cd9b5862-6a67-ba57-4c30-3e0a8c58630a%22%2C%22e%22%3A1706639075877%2C%22c%22%3A1706637275877%2C%22l%22%3A1706637275877%7D; ab.storage.deviceId.cd97b079-ff05-4967-873a-324050c2a198=%7B%22g%22%3A%22530dbd9f-cdb8-b085-4a1e-1c863805d5a7%22%2C%22c%22%3A1706637275878%2C%22l%22%3A1706637275878%7D; cto_bundle=Y50NSl9wNkVkejMwUVQlMkYzaWRwTmpmQTQ0OHhjU2FwN05ZJTJCaWZpd1dkcVdDWFolMkIyZnVSaTUzbmJHOVZSWmtrcjZIdHhNbTM5WGxnMzNtSWt4eFFjVldCc0wyMVRnVnhURHpocnBjbG5uRnhaUnZOSTg2YSUyRmtYRThBT244bWhjSmZnUkhrd0lteHRhN3RLcjUweXQlMkJpUlM1WmZFUktySjNqWUUlMkY1SU5ZdiUyQjU0ajBNMCUzRA; _gid=GA1.2.61054937.1706890192; ECCS=; CAPTGM=fzfgvqmzEOuQL/biwIqD5Q==; TMem%5FNO%5FG=T30079727; TMem%5FNO=T30079727; cbtUser=OgXk2tGvtQokTXllUDEXJWKlWuo5M8BgZOdNUOBbTow=; memID=nByjUC0fTjo%2BSesU2nY2XMiJ8vOQNSKMtAXgQRqEqUE%3D; memNo=Uvur4fPd%2BoFPmQLVVE3w6Q%3D%3D',
}
payload=None

response0 = requests.request("GET", "https://gpoticket.globalinterpark.com/Global/Play/Book/BookSeatDetail.asp?GoodsCode=24000291&PlaceCode=24000014&LanguageType=G2001&MemBizCode=10965&PlaySeq=001&SeatGrade=&Block=RGN001&TmgsOrNot=D2006&LocOfImage=24000014.gif&Tiki=N&UILock=Y&SessionId=30211BAC2F7045B6B692D31BD31B89D4&BizCode=10965&GoodsBizCode=35736&GlobalSportsYN=N&SeatCheckCnt=0", headers=headers, data=payload)
print(response0.text)
soup = BeautifulSoup(response0.content, 'html.parser')

# 使用BeautifulSoup查找元素值
value = soup.find_all('img')

# 打印元素值
for v in value:
    print(v.get('onclick'))