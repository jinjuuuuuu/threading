import requests

url = "http://127.0.0.1:5000/start"
data = {"input": "테스트"}

response = requests.post(url, json=data)
print(response.json())