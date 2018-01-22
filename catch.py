from bs4 import BeautifulSoup
import requests
import json
import mysql.connector
conn = mysql.connector.connect(user='root', password='root', database='tydatabase')
cursor = conn.cursor()
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
def catchAction(m, d, data):
	try:
		soup = BeautifulSoup(requests.get("http://www.todayonhistory.com/" + str(m) + '/' + str(d) + '/', headers=headers).content, 'html.parser', from_encoding='utf-8')
		imgDiv = soup.find_all('div', 'pic')
		subArr = []

		for index, iD in enumerate(imgDiv):
			if iD.a and iD.a.img:
				temp = iD.a.img
				src = temp['data-original']
				if src[0] == '/':
					src = 'http://www.todayonhistory.com' + src
				subArr.append({'src': src, 'year': iD.find_previous_sibling().span.b.text, 'title': temp['alt']})
		i = 1

		while i < 4:
			conten = json.loads(requests.get("http://www.todayonhistory.com/index.php?m=content&c=index&a=json_event&page=%s&pagesize=40&month=%s&day=%s" % (str(i), str(m), str(d)), headers=headers).content)
			if conten == 0:
				i = 4
			else:
				for index, item in enumerate(conten):
					src = item['thumb']
					if len(src) > 0:
						if src[0] == '/':
							src = 'http://www.todayonhistory.com' + src
						subArr.append({'src': src, 'year': item['solaryear'], 'title': item['title']})
			i = i + 1

		data.append((str(m*100 + d), json.dumps(subArr)))
	except Exception as e:
		print('Error:', e)
	
	
mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# mon = [2]
for index, item in enumerate(mon):
	result = []
	for i in range(item):
		m = index + 1
		d = i + 1
		catchAction(m, d, result)
	# cursor.execute(sql)
	# execute执行单条sql语句，executemany执行多条
	try:
		cursor.executemany('insert into history_today (date, result) values (%s, %s)', result)
		conn.commit()
	except Exception as e:
		print('Error:', e)
cursor.close()
