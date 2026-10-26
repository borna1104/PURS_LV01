import requests

response = requests.delete('http://192.168.83.5/temperatura?id=4')

for k, v in response.headers.items():
    print(f'{k}: {v}')

print(response.text)
print(response.status_code)