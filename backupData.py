import requests
import time
import subprocess
import os


now = time.time()
files = os.listdir()
for file in files:
	if now - os.stat(file).st_ctime > 4 * 24 * 3600:
		os.remove(file)

timeStr = time.strftime("%m-%d", time.localtime())
f = open('%s_gateway.zip' % (timeStr), 'wb')
f2 = open('%s_gateway_ext.zip' % (timeStr), 'wb')
api = 'https://mock.lechebang.cn/api/mock/export'
# gateway
soa = requests.post(api, data={'project_id': '5b69520ca74f031492f4c489'})
# gateway_ext
php = requests.post(api, data={'project_id': '5b7294e5a74f031492f4c527'})
f.write(soa.content)
f2.write(php.content)
f.close()
f2.close()
subprocess.call('git add . && git commit -m "脚本提交" && git push', shell=True)

# crontab -e
# 30 18 * * 1-5 cd /Users/tangyang/Desktop/lechebang/server/mockData && /Users/tangyang/anaconda3/bin/python3 getData.py > /dev/null