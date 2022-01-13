import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)
spot_data=data["result"]["results"]
with open("data.csv","w",encoding="UTF-8-sig") as file:
    for spot_item in spot_data:
        spot_item['address']=spot_item['address'][5:8]
        img_list=spot_item['file']
        img=img_list.split('https://')
        file.write(spot_item['stitle']+","+spot_item['address']+","+spot_item['longitude']+","+spot_item['latitude']+","+"https://"+img[1]+"\n") 


    


