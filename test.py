import requests

BASE="http://127.0.0.1:5000/"


data=[{"name":"avishek","views":1000,"likes":10},
        {"name":"avishekd","views":10000,"likes":101},
        {"name":"avishekb","views":100011,"likes":1},
        {"name":"avishekc","views":11000,"likes":1110}]

for i in range(len(data)):
    response=requests.put(BASE+'video/'+str(i),data[i])
    print(response.json())

input()
response=requests.delete(BASE+'video/0')
print(response)
input()
response=requests.get(BASE+'video/3')
print(response.json())