import requests
from pprint import pprint


# читаем токен
with open('token.txt', 'r') as file_object:
    token = file_object.read().strip()

name_hero = ['Hulk', 'Captain America', 'Thanos']
result_dict = {}
new_list=[]
for item in name_hero:
    URL = 'https://superheroapi.com/api/'+token+'/search/'+item
    response = requests.get(URL).json()
    res = response['results']

    for name in res:
            if name['name'] == item:
                result_dict[item] = int(name['powerstats']['intelligence'])

max_val = max(result_dict.values())
final_dict = {k:v for k, v in result_dict.items() if v == max_val}

pprint(f' Победил {final_dict}')