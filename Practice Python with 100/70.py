import requests
response = requests.get("https://pythonhow.com/data/universe.txt", headers = {'user-agent': 'customUserAgent'})
text = response.text
print(text)
