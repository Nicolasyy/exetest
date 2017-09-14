#!/usr/bin/python2
# coding=utf-8
import requests
#
# pars = {"user_id":"ZZ290","tenant_id":"dev","task_id":"TASK_544","answers":[{"exercise_id":"02767","score":50,"answer":[2],"options":[2,3,4,1]},{"exercise_id":"02761","score":50,"answer":[],"options":[2,4,1,3]}],"spent_time":7,"local_spent_time":6.958,"submit_type":0,"timestamp":1504511620309}
# url = 'https://tests.exexm.com:800/api/Exam/Post/Anonymous'
# r = requests.post(url, json=pars)
# print r.text

url1 = 'http://123.56.181.210:8001/api/login'
json = {
    "tenantId": "dev",
    "userId": "ZZ290",
    "pwd": "123456",
    "plat_form": 0,
    "language": "zh-cn"
}
r = requests.post(url1, json=json)
token = r.json()['data']['ticket']
print token
# url2 = 'https://tests.exexm.com:800/api/Exam'
# json1 = dict(task_id="TASK_544", answers=[{"exercise_id": "02767", "score": 50, "answer": [2], "options": [2, 3, 4, 1]},
#                                           {"exercise_id": "02761", "score": 50, "answer": [3],
#                                            "options": [2, 4, 1, 3]}], spent_time=7, local_spent_time=6.958,
#              submit_type=0, timestamp="1504511620309")
# headers = {'token': token}
# r1 = requests.post(url2, json=json1, headers=headers)
# print r1.content
url2 = 'https://tests.exexm.com:800/api/Knows'
JSON = {"content":'1111',
        "invite_users": [],
        "is_from_colleagues": "",
        "labels": []}
headers = {'token': token}
r1 = requests.post(url2, json=JSON, headers=headers)
print r1.content
