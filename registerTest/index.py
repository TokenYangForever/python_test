import requests

# 当当网 dangdang
def registerDangdang (mobile):
	headers = {
		'Accept': '*/*',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
		'Connection': 'keep-alive',
		'Content-Length': '18',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Cookie': '__permanent_id=20180507163324780145962454489126627; ddscreen=2; dest_area=country_id%3D9000%26province_id%3D111%26city_id%20%3D0%26district_id%3D0%26town_id%3D0; permanent_key=20180507163216172005142855bb70df; __visit_id=20180507173817143243414299670154586; __out_refer=; __dd_token_id=20180507174337108067355157b1ff17; __trace_id=20180507174450522342457211413415220; login.dangdang.com=.AYH=20180507174337053729204&.ASPXAUTH=; __rpm=register_page...1525686284451%7Cregister_page...1525686307649',
		'Host': 'login.dangdang.com',
		'Origin': 'https://login.dangdang.com',
		'Referer': 'https://login.dangdang.com/register.php?returnurl=http://www.dangdang.com/',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest',
	}
	try:
		r = requests.post('https://login.dangdang.com/p/mobile_checker.php', data = {'mobile': mobile}, headers = headers)
		print(r.content)
	except Exception as e:
		print('Error:', e)

registerDangdang(18382436735)