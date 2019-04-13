#! python3
##get weather
import json,requests,sys,time,datetime

location = ['阳谷','沈阳']
for i in range(len(location)):
	url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + location[i]

	print('当前时间：' + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
	try:
		response = requests.get(url)
		response.raise_for_status()
	except Exception as exce:
		print('There was a problem: %s' % (exce))
		time.sleep(5)
		sys.exit(0)
	weatherData = json.loads(response.text)
	w = weatherData['data']
	wf = w['forecast']
    
	print('%s当前的天气状况：' % (w['city']) + wf[0]['type'])
	print('当前气温：' + w['wendu'])
	print('今天气温预测：      ' + wf[0]['low'] + wf[0]['high'] + '	' + wf[0]['type'] + '	风力' + wf[0]['fengli'][8:14])
	print('明天气温预测：      ' + wf[1]['low'] + wf[1]['high'] + '	' + wf[1]['type'] +  '	风力' + wf[1]['fengli'][8:14])
	print('%s气温预测：' %(wf[2]['date']) + wf[2]['low'] + wf[2]['high'] + '  ' + wf[2]['type'] +  '	风力' + wf[2]['fengli'][8:14])
	print('%s气温预测：' %(wf[3]['date']) + wf[3]['low'] + wf[3]['high'] + '  ' + wf[3]['type'] +  '	风力' + wf[3]['fengli'][8:14])
	print('%s气温预测：' %(wf[4]['date']) + wf[4]['low'] + wf[4]['high'] + '  ' + wf[4]['type'] +  '	风力' + wf[4]['fengli'][8:14] + '\n')

time.sleep(1)