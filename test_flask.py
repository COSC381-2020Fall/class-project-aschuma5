import requests 

url = 'http://127.0.0.1:5000/query?q=40k&p=1'
response = request.get(url)
result = response.json()
print(result)
