import requests


response = requests.get('http://192.168.83.5/temperatura')

for k, v in response.headers.items():
    print(f'{k}: {v}')

print(response.json().get("temperatura"))
print(response.status_code)