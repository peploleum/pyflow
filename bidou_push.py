# -*- coding: UTF-8 -*-
import http.client

print("establishing connection with rest Endpoint")
conn = http.client.HTTPConnection('localhost', 8080)
print("connection established")
params = open('bidou.json', 'r', encoding="utf-8")
read = params.read()
print(read)
headers = {"Content-type": "application/json; charset=UTF-8",
           "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImF1dGgiOiJST0xFX0FETUlOLFJPTEVfVVNFUiIsImV4cCI6MTUyNzA4NDEyMX0.KhgPn36XmG2jPnEfhMDAlYD0O4QJLuP1NjygAUDxe7fM1-RPHVyoVONmSeUo1vcTvxpwKCI4-w2vG9OYgQx-aw"}
print("POSTING BIDOU")
conn.request("POST", '/api/bidous', read, headers)
print("Getting response")
response = conn.getresponse()
responseCode = response.getcode()
print("RESPONSE POST BIDOU " + str(responseCode))
conn.close()

print("establishing connection with rest Endpoint")
conn = http.client.HTTPConnection('localhost', 8080)
print("connection established")
headers = {"Accept": "application/json; charset=UTF-8",
           "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImF1dGgiOiJST0xFX0FETUlOLFJPTEVfVVNFUiIsImV4cCI6MTUyNzA4NDEyMX0.KhgPn36XmG2jPnEfhMDAlYD0O4QJLuP1NjygAUDxe7fM1-RPHVyoVONmSeUo1vcTvxpwKCI4-w2vG9OYgQx-aw"}
print("GETTING BIDOU")
conn.request("GET", '/api/specificBidou', None, headers)
print("Getting response")
response = conn.getresponse()
responseCode = response.getcode()
response_read = response.read()
print("RESPONSE GET BIDOU " + str(responseCode))
print("RESPONSE GET BIDOU CONTENT " + str(response_read))
conn.close()
