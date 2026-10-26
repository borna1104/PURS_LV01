import requests

response = requests.get('https://api.ipify.org/?format=json')

for k, v in response.headers.items():
    print(f'{k}: {v}')

print(response.json().get('ip'))