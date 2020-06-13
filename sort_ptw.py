import json
import xmltodict
import time
from jikanpy import Jikan


with open("animelist.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
xml_file.close()
ani_list = json.dumps(data_dict)
ani_list = json.loads(ani_list)

ptw = []
for i in ani_list['myanimelist']['anime']:
    if i['my_status'] == 'Plan to Watch':
        ptw.append(i['series_title'])

jikan = Jikan()
ptw_scores = []
for i in ptw:
    anime_name = i
    anime = jikan.search(search_type="anime", query=anime_name)
    for k in anime['results']:
        if k['title'].lower() == anime_name.lower():
            ptw_scores.append({'title': i, 'score': k['score']})
            break
    time.sleep(4)

list = {'sorted_ptw': sorted(ptw_scores, key=lambda ani: ani['score'], reverse=True)}

f = open("sorted PTW list.txt", "w")
f.write(json.dumps(list, indent=4, sort_keys=True))
f.close()
