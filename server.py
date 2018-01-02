from flask import Flask
from flask import request
from flask import jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/historyToday', methods=['GET'])
def historyToday():
	soup = BeautifulSoup(requests.get("http://www.todayonhistory.com/").content, 'html.parser', from_encoding='utf-8')
	# 年份
	moh = list(map(lambda x: x.b.text, soup.find_all('span', 'moh')))
	# 图片
	result = []
	imgDiv = soup.find_all('div', 'pic')
	for index, iD in enumerate(imgDiv):
		if iD.a and iD.a.img:
			temp = iD.a.img
			src = temp['data-original']
			if src[0] == '/':
				src = 'http://www.todayonhistory.com' + src
			result.append({'src': src, 'year': moh[index], 'title': temp['alt']})

	return	jsonify({'result': result})

app.run()