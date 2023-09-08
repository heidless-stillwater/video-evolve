import requests

BASE = 'http://localhost:5000/'

data = [
  {"name":"tim", "likes":10, "views":10000},
  {"name":"amy", "likes":1000, "views":2000},
  {"name":"bryan", "likes":100000, "views":30},
]

for i in range(len(data)):
  response = requests.put(BASE + "video/" + str(i), data[i])
  print(response.json())

response = requests.delete(BASE + "video/0")
print(response)

#input()

#response = requests.put(BASE + "video/1", {"name":"tim", "likes":10, "views":10000})
#print(response.json())
#input()

#input()

#response = requests.get(BASE + "video/2")
#print(response.json())