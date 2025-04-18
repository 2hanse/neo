import json

data = {'age':30, 'name':'홍길동', 'address':'마포구 공덕동', \
        'broadcast' : {
            'sbs' : 5, 'kbs' : 9, 'mbc' : 11
        }
}

json_str = json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True)     #json을 저장하는 방법. 위에 저장된 데이터를 json 파일 형태로 만들 수 있음.
print(json_str)
print(type(json_str))
print('-' * 50)

json_data = json.loads(json_str)
print(json_data)
print(type(json_data))
print('-' * 50)

print(json_data['name'])
print(json_data['age'])
print(json_data['broadcast']['mbc'])
print('-' * 50)

print('finished.')