# -*- coding: UTF-8 -*-
import http.client

print("establishing connection with rest Endpoint")
conn = http.client.HTTPConnection('localhost', 8090)
print("connection established")
print("calling GET")
conn.request("GET", '/entry-point/test2')
print("Getting response")
response = conn.getresponse()
responseCode = response.getcode()
print("RESPONSE GET " + str(responseCode))
conn.close()

print("establishing connection with rest Endpoint")
conn = http.client.HTTPConnection('localhost', 8090)
print("connection established")
params = 'payload'
headers = {"Content-type": "text/plain"}
print("calling POST")
conn.request("POST", '/entry-point/push', params, headers)
print("Getting response")
response = conn.getresponse()
responseCode = response.getcode()
print("RESPONSE POST " + str(responseCode))
conn.close()

print("establishing connection with rest Endpoint")
conn = http.client.HTTPConnection('localhost', 8090)
print("connection established")
# params = open('payload.txt', 'r', encoding="utf-8")
params = open('payload.json', 'r', encoding="utf-8")
read = params.read()
print(read)
headers = {"Content-type": "application/json; charset=UTF-8"}
print("POSTING FILE")
conn.request("POST", '/entry-point/post', read, headers)
print("Getting response")
response = conn.getresponse()
responseCode = response.getcode()
print("RESPONSE POST " + str(responseCode))
conn.close()
