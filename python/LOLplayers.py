import requests
import json
#აქ არის თამაში league of legends ერთი გუნდის მონაცემები და ამ გუნდიდან გამოქვს მოთამაშის სახელი და გვარი, ასევე იწერს გუნდის ლოგოს



url_image = 'http://static.lolesports.com/teams/1631819402484_lng-2021-worlds.png'

url = "https://league-of-legends-esports.p.rapidapi.com/teams"

querystring = {"id":"lng-esports"}

headers = {
	"X-RapidAPI-Host": "league-of-legends-esports.p.rapidapi.com",
	"X-RapidAPI-Key": "ef9e4cf392msh28a220ad18b49ddp1197eejsn708559e6e8ff"
}

response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.text)
result_json = response.text
resu = json.loads(result_json)
res_structured = json.dumps(resu, indent=4)
print(res_structured)

with open('lol_team.json', 'w') as file1:
	file1.write(res_structured)

m = resu["players"]
player_name = m["firstName"]
player_lname = m["lastName"]
print("მოთამაშის სახელია: ", player_name)
print("მოთამაშის გვარია: ", player_lname)
print(m)

res = requests.get(url)
print(res)
print(res.status_code)
print(res.headers)
print(res.headers['Connection'])

res_img = requests.get(url_image)
img_file = open('img1.png', 'wb')
img_file.write(res_img.content)
img_file.close()

