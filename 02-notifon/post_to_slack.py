# coding: utf-8
import requests
url = '' # replace with slack webhook url
data = { "text" : "Hello, world." }
requests.posturl, json=data)
requests.post(url, json=data)
