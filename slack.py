import os
import requests
from datetime import datetime

start_mes = '''
今日のタスクどうぞ
1.
2.
3.
今日も頑張ってこー
'''[1:-1]

an_hour_mes = '''
1時間経過！進捗どう？

①やったこと
②次やること
③メモ

休憩挟みつつ頑張ろう！
'''[1:-1]

end_mes = '''
おつ！終了！

①今日やったことを報告！
②学びはTwitterにまとめといて
'''[1:-1]

now_hour = datetime.now().hour
if now_hour < 13:
   message = start_mes
elif now_hour > 19:
   message = end_mes
else:
   message = an_hour_mes

# スラック
TOKEN = os.environ['REMIND_SLACK_TOKEN']
CHANNEL = 'つみあげ'

url = "https://slack.com/api/chat.postMessage"
headers = {"Authorization": "Bearer "+ TOKEN}
data  = {
   'channel': CHANNEL,
   'text': message
}
res = requests.post(url, headers=headers, data=data)
res.json