#! python3
#获取每天城市天气,通过url获取json数据，然后根据json格式解析相关数据，下面实际是两个程序分别从不同的网站获取数据

import json,requests,sys
#分别两个不同的网站获取数据，经验证第一个数据更为准确
def getweather(location):
	url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + location

	response = requests.get(url)
	response.raise_for_status()
	weatherData = json.loads(response.text)
	w = weatherData['data']
	wf = w['forecast']

	print('%s当前的天气状况：' % (w['city']) + wf[0]['type'])
	print('当前气温：' + w['wendu'])
	print('今天气温预测：      ' + wf[0]['low'] + wf[0]['high'] + '	' + wf[0]['type'] + '	风力' + wf[0]['fengli'][8:14])
	print('明天气温预测：      ' + wf[1]['low'] + wf[1]['high'] + '	' + wf[1]['type'] +  '	风力' + wf[1]['fengli'][8:14])
	print('%s气温预测：' %(wf[2]['date']) + wf[2]['low'] + wf[2]['high'] + '  ' + wf[2]['type'] )
	print('%s气温预测：' %(wf[3]['date']) + wf[3]['low'] + wf[3]['high'] + '  ' + wf[3]['type'])
	print('%s气温预测：' %(wf[4]['date']) + wf[4]['low'] + wf[4]['high'] + '  ' + wf[4]['type'] + '\n')

'''
两种输入城市参数的方法，第一种为非交互式，通过命令行带参数，这种好处是方便其他函数对该函数的引用；
第二种是用户输入城市，然后实时查询
执行py.exe .\weather.py 北京
if len(sys.argv) < 2 :
	print('请输入要查询城市名称！')
	sys.exit()
location = ''.join(sys.argv[1:])
'''
location = input('请输入要查询城市名称:')
while location :
	if location == 'exit' :
		print('系统即将退出')
		sys.exit()
	else:
		try:
			getweather(location)
		except Exception as exw:
			print('%s 不符合城市名称规范,请重新输入！' % (location) )
	
	location = input('请输入要查询天气的城市名称:')
			
	
##另一个网站只支持通过城市代码获取天气,weather2.json
#沈阳和阳谷的天气
# location = ['101070101']
# for i in range(len(location)):
	# url = 'http://t.weather.sojson.com/api/weather/city/' + location[i]

	# response = requests.get(url)
	# response.raise_for_status()

	# weatherData = json.loads(response.text)
	# w = weatherData['data']
	# wc = weatherData['cityInfo']
	# wf = w['forecast']

	# print('数据更新时间：' + weatherData['time'])
	# print('%s当前的天气状况：' % (wc['city']) )
	# print('温度：' + w['wendu'])
	# print('空气质量：' + w['quality'])
	# print('明天天气预测：' + wf[0]['low'] + '-' + wf[0]['high'] )
