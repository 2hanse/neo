import json, urllib.request, datetime, math
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath('./')))
secret_file = os.path.join(BASE_DIR, '../../secret.json')

with open(secret_file) as f:                   
    secrets = json.loads(f.read())             # json.load로 불러오면 list로 불러옴.

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getHospitalData(pageNo, numOfRows):
    end_point='https://apis.data.go.kr/6260000/MedicInstitService/MedicalInstitInfo'
    
    paramter = ''
    paramter += "?resultType=json"
    paramter += "&serviceKey=" + get_secret('data_apiKey')
    paramter += "&pageNo=" + str(pageNo)
    paramter += "&numOfRows=" + str(numOfRows)
    url = end_point + paramter
    
    print("URL : ")
    print(url)

    result = getRequestUrl(url)
    if (result == None):
        return None
    else:
        return json.loads(result)

jsonResult = []

pageNo = 1
numOfRows = 100
nPage = 0

while True:                                                 # 출력해봐야 어떤 타입인지 알 수 있기에 출력하는 과정. (item이 여러개이기 때문에 반복문 사용.)
    print('pageNo : %d, nPage : %d' % (pageNo, nPage))
    jsonData = getHospitalData(pageNo, numOfRows)
    print(jsonData)

    if (jsonData['response']['header']['resultCode'] == '00'):
        totalCount = jsonData['response']['body']['totalCount']
        print('데이터 총 개수 : ', totalCount)  

        for item in jsonData['response']['body']['items']['item']:         # 실제 item이 들어 있는 장소.
            jsonResult.append(item)

        if totalCount == 0:
            break
        nPage = math.ceil(int(totalCount) / int(numOfRows))
        if (pageNo == nPage):  
            break  

        pageNo += 1
    else :
        break

    savedFilename = 'p515_BusanHospital.json'
    with open(savedFilename, 'w', encoding='utf-8') as outfile:
        resJson = json.dumps(jsonResult, indent=4, ensure_ascii=False, sort_keys=True)
        outfile.write(resJson)
    
    print(savedFilename + ' file saved..')

# 출력값 : ~.json : dictionary 타입. dict 타입이기 때문에, key & value가 있음.