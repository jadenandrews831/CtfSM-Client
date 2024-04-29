from bs4 import BeautifulSoup as bs
from datetime import date

import json
import requests
import socket
import urllib.parse

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
print(f"IP: {IP}")

url = "http://10.190.110.24/api/Challenges/?sort=solved"
r = requests.get(url)
print("This program is working")

app_data = json.loads(r.content)["data"]
app_data.reverse()

data_dict = dict()
i = 0

for el in app_data:
    # name = el[]
    # print(el['solved'], el['id'], el['name'], el['difficulty'])
    if el['solved'] == True:
        data_dict[f"{i}"] = [el['name'], str(el['difficulty']), IP, str(date.today())]
        i += 1
    else:
        break


data_dict = urllib.parse.quote(str(data_dict)).replace('%27', '%22')
print(f"data_dict: {data_dict}")
u = f'http://10.190.110.39:8080/upload?data={data_dict}'
x = requests.post(u)
print("X:",x)
print(x.text)
