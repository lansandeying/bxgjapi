import requests
from ddt_data.data_29009 import url
headers={
    
    }
data={
    "transType": "29009",
    "data": '{"activityId":"5555","enterpriseNo":"123456","oneKey":"pwY6A-v1divh-1L4331-WF3Xp7-cTnAf","cjNo":"gg-2"}'
    }

r=requests.post(url=url,data=data)

print(r.json())