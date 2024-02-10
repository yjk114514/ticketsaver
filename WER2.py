import requests
import base64

headers = {
 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/23018604 Firefox/122.0',
 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
 'accept-language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
 'accept-encoding':'gzip, deflate, br',
 'content-type':'application/x-www-form-urlencoded',
 'content-length':'326',
 'origin':'https://gpoticket.globalinterpark.com',
 'referer':'https://gpoticket.globalinterpark.com/Global/Play/Book/BookSeat.asp?'
           'GoodsCode=23018604'
           '&PlaceCode=23001777'
           '&OnlyDeliver=68006'
           '&DBDay=12&ExpressDelyDay=0'
           '&GroupName=2024+%EF%BC%86TEAM+CONCERT+TOUR+%E2%80%98FIRST+PAW+PRINT%E2%80%99+IN+SEOUL'
           '&PlaceName=KBS%EC%95%84%EB%A0%88%EB%82%98'#蓝色广场+万事达卡厅
           '&TmgsOrNot=D2003'
           '&LocOfImage='
           '&Tiki=N'
           '&KindOfGoods=01003'
           '&GlobalSportsYN=N'
           '&isSeatCntView=Y'
           '&LanguageType=G2001'
           '&MemBizCode=10965'
           '&BizCode=10965'
           '&PlayDate=20240217'
           '&PlaySeq=001'
           '&SessionId=C0C1AFC225F54DC9BD6AC6475D284D3F'
           '&BizMemberCode=T30078660'
           '&BizMemberFlag='
           '&GoodsBizCode=35736'
           '&WynsCode=&WynsGateID=&PageCV=',
 'upgrade-insecure-requests':'1',
 'sec-fetch-dest':'iframe',
 'sec-fetch-mode':'navigate',
 'sec-fetch-site':'same-origin',
 'sec-fetch-user':'?1',
 'te':'trailers',
 'cookie':'_ga_BEN1B7STVY=GS1.1.1707196351.14.1.1707197493.0.0.0; _ga=GA1.2.925805744.1706529252; _fbp=fb.1.1706529254918.749465469; _ga_4SKTL7E8Q8=GS1.1.1706637275.1.0.1706637286.49.0.0; ab.storage.sessionId.cd97b079-ff05-4967-873a-324050c2a198=%7B%22g%22%3A%22cd9b5862-6a67-ba57-4c30-3e0a8c58630a%22%2C%22e%22%3A1706639075877%2C%22c%22%3A1706637275877%2C%22l%22%3A1706637275877%7D; ab.storage.deviceId.cd97b079-ff05-4967-873a-324050c2a198=%7B%22g%22%3A%22530dbd9f-cdb8-b085-4a1e-1c863805d5a7%22%2C%22c%22%3A1706637275878%2C%22l%22%3A1706637275878%7D; cto_bundle=Y50NSl9wNkVkejMwUVQlMkYzaWRwTmpmQTQ0OHhjU2FwN05ZJTJCaWZpd1dkcVdDWFolMkIyZnVSaTUzbmJHOVZSWmtrcjZIdHhNbTM5WGxnMzNtSWt4eFFjVldCc0wyMVRnVnhURHpocnBjbG5uRnhaUnZOSTg2YSUyRmtYRThBT244bWhjSmZnUkhrd0lteHRhN3RLcjUweXQlMkJpUlM1WmZFUktySjNqWUUlMkY1SU5ZdiUyQjU0ajBNMCUzRA; _gid=GA1.2.1296783177.1707196592; cbtUser=OgXk2tGvtQokTXllUDEXJWh7o4J6oy4OyaLa+F/QTFw=; memID=nByjUC0fTjo%2BSesU2nY2XMiJ8vOQNSKMtAXgQRqEqUE%3D; memNo=Uvur4fPd%2BoFPmQLVVE3w6Q%3D%3D; TMem%5FNO=T30079727; TMem%5FNO%5FG=T30079727; ECCS=OIJMGwGU2QwUKPmZajidF6hzaoAardgvaaoZZio1bVGAE9c55vR9PfuMedyZwc1T; CAPTGM=Vn3OqZK5Yze7mTAEt3UdOQ=='}

payload=(b'Flag=Blocking'
         b'&GoodsCode=24000291'
         b'&PlaceCode=24000014'
         b'&PlaySeq=001'
         b'&SessionId=C0C1AFC225F54DC9BD6AC6475D284D3F'
         b'&LanguageType=G2001'
         b'&BizCode=10965'
         b'&MemBizCode=10965'
         b'&GoodsBizCode=23018604'
         b'&SeatCnt=1'
         b'&SeatGrade=1%5E'
         b'&Floor=%EA%B0%9D%EC%84%9D1%EC%B8%B5%5E'#观众席1楼
         b'&RowNo=A%EA%B5%AC%EC%97%AD+%EC%9E%85%EC%9E%A5%EB%B2%88%ED%98%B8%5E'#A区+入场号
         b'&SeatNo=1%5E'
         b'&CTCYN=Y')

# 打印编码后的字符串
#SeatGrade, Floor, RowNo, SeatNo, Block
response0 = requests.request("POST", "https://gpoticket.globalinterpark.com/Global/Play/Book/Lib/BookInfo.asp", headers=headers, data=payload)

print(response0.text)