import requests, json, time, datetime, html, re
url = 'https://traodoisub.com/api/?fields=reaction&access_token=TDS9JCMxIXZ2V2ciojIyVmdlNnIsICNzITMu92co5WYwlmViojIyV2c1Jye'   
response = requests.get(url)
data =  json.loads(response.text)
print(data)
if 'countdown' in data:
        countdown_value = data['countdown']
        for i in range(int(countdown_value) + 5, 0, -1):
            print(f'Thao tác quá nhanh vui lòng chậm lại, đợi {i} giây', end='\r')
            time.sleep(1)
            continue
else:
    id_list = [item['id'] for item in data]
    print(id_list)