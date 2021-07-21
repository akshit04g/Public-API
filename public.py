#! C:/Python39/python.exe

print("Content-Type: text/html\n")

import requests

url="https://api.publicapis.org/entries?category=art"

payload={}
headers={}

response = requests.request("GET",url,headers=headers,data=payload)

print(response.text)