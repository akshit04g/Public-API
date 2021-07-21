#! C:/Python39/python.exe

print("Content-Type: text/html\n")

import requests

url="https://datausa.io/api/data?drilldowns=Nation&measures=Population"
url1='https://catfact.ninja/fact'
url2="https://dog.ceo/api/breeds/image/random"

payload = {}
headers = {}

response1 = requests.request("GET", url, headers=headers, data=payload)
response2 = requests.request("GET", url1, headers=headers, data=payload)
response3 = requests.request("GET", url2, headers=headers, data=payload)


print(response1.text)
print(response2.text)
print(response3.text) 