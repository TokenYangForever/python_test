from bs4 import BeautifulSoup
import requests
import json

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Host': 'www.todayonhistory.com',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}

# mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mon = [3]
for index, item in enumerate(mon):
	for i in range(item):
		m = index + 1
		d = i + 1
		soup = BeautifulSoup(requests.get("http://www.todayonhistory.com/" + str(m) + '/' + str(d) + '/', headers=headers).content, 'html.parser', from_encoding='utf-8')
		result = []
		imgDiv = soup.find_all('div', 'pic')
		for index, iD in enumerate(imgDiv):
			if iD.a and iD.a.img:
				temp = iD.a.img
				src = temp['data-original']
				if src[0] == '/':
					src = 'http://www.todayonhistory.com' + src
				result.append({'src': src, 'year': iD.find_previous_sibling().span.b.text, 'title': temp['alt']})
		print(len(result))

