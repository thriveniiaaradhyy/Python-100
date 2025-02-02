import requests

response = requests.get("https://pythonhow.com/data/universe.txt", headers = {'user-agent': 'customUserAgent'})

text = response.text
words = text.count("a")
print(words)
