from flask import Flask, request, jsonify, make_response
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/historyToday', methods=['GET'])
def historyToday():
	soup = BeautifulSoup(requests.get("http://www.todayonhistory.com/").content, 'html.parser', from_encoding='utf-8')
	result = []
	imgDiv = soup.find_all('div', 'pic')
	for index, iD in enumerate(imgDiv):
		if iD.a and iD.a.img:
			temp = iD.a.img
			src = temp['data-original']
			if src[0] == '/':
				src = 'http://www.todayonhistory.com' + src
			result.append({'src': src, 'year': iD.find_previous_sibling().span.b.text, 'title': temp['alt']})

	response = make_response(jsonify({'result': result}))
	# 设置cors 允许跨域
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'POST'
	response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
	return	response
app.run()