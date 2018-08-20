import requests
import time
import subprocess
timeStr = time.strftime("%m-%d", time.localtime())
f = open('%s_gateway.zip' % (timeStr), 'wb')
f2 = open('%s_gateway_ext.zip' % (timeStr), 'wb')
# gateway
soa = requests.post('https://mock.lechebang.cn/api/mock/export', data={'project_id': '5b69520ca74f031492f4c489'})
# gateway_ext
php = requests.post('https://mock.lechebang.cn/api/mock/export', data={'project_id': '5b7294e5a74f031492f4c527'})
f.write(soa.content)
f2.write(php.content)
f.close()
f2.close()
subprocess.call('git add . && git commit -m "脚本提交" && git push', shell=True)

# crontab -e
# 30 18 * * * cd /Users/tangyang/Desktop/lechebang/server/mockData && /Users/tangyang/anaconda3/bin/python3 getData.py