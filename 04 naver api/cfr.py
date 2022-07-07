# Clova Face Recognition

import os, sys, requests, json
from pprint import pprint

client_id = '4kHXLHhXYI67SCnP77en'
client_secret = 'g_q6FN3k0t'

url = 'https://openapi.naver.com/v1/vision/face' # 얼굴 감지


files = {'image' : open('test.jpg', 'rb')}
headers = {'X-Naver-Client-Id' : client_id, 'X-Naver-Client-Secret' : client_secret}

response = requests.post(url, files=files, headers=headers)
rescode = response.status_code

if (rescode==200):
    '''
    print (response.text)
    data = json.loads()
    '''
    data = json.loads(response.text) # 딕셔너리로 반환
    pprint(data)
    print(type(data))
    print(data['info']['faceCount'])  # 이중 딕셔너리
else:
    print('Error Code:' + rescode)