import requests
from pprint import pprint
import datetime

todate = datetime.date.today().strftime("%Y-%m-%d")
fromdate = (datetime.date.today() - datetime.timedelta(days = 2)).strftime("%Y-%m-%d")
param = {'fromdate':fromdate,'todate':todate, 'order':'desc','sort':'activity','tagged':'python','filter':'default', 'site':'stackoverflow'}
header = {'Content-Type': 'application/json'}
resp = requests.get('https://api.stackexchange.com/2.3/questions', params = param, headers = header).json()
# Обеспечивается вывод информации по вопросам в виде нумерованного списка с указанием темы вопроса и ссылке, по которой можно перейти к его телу
quest_id = [f"{id+1}.Вопрос: {val['title']} по ссылке: {val['link']}" for id,val in enumerate(resp['items'])]

pprint(quest_id)


