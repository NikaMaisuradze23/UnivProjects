import requests
import json
import sqlite3

url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone-matches/Amartin743/psn"
img_url = "https://imgs.callofduty.com/content/dam/atvi/callofduty/cod-touchui/vanguard/seasons/season-3/battlepass/battle-pass-tout-desktop.jpg"

headers = {
	"X-RapidAPI-Host": "call-of-duty-modern-warfare.p.rapidapi.com",
	"X-RapidAPI-Key": "ef9e4cf392msh28a220ad18b49ddp1197eejsn708559e6e8ff"
}

response = requests.request("GET", url, headers=headers)
# print(response.text)
result_json = response.text
resu = json.loads(result_json)
res_structured = json.dumps(resu, indent=4)
# print(res_structured)


#სერვერის სტატუსი
res = requests.get(url)
print(res)
print(res.status_code)
print(res.headers)
print(res.headers['Date'])

#კონკეტული მოთამაშის სტატისტიკის გამოტანა
m = resu['summary']
all = m['all']
kills = all['kills']
death = all['deaths']
asist = all['assists']
print("მოთამაშემ მოკლა: ", kills, " სამხედრო/რობოტი")
print("მოთამაშე მოკვდა: ", death, "-ჯერ")
print("მოთამაშემ აიღო: ", asist, " ასისტი")

#ფაილში შენახვა მონაცემების
with open('cod_team.json', 'w') as file1:
	file1.write(res_structured)

#გუნდის სურათის ჩამოტვირთვა
res_img = requests.get(img_url)
img_file = open('CallOfDuty.png', 'wb')
img_file.write(res_img.content)
img_file.close()

#ბაზაში მონაცემების დამატება
conn = sqlite3.connect("COD.sqlite")
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE callod
# 				(id INTEGER PRIMARY KEY AUTOINCREMENT,
# 				kills VARCHAR(100),
# 				death VARCHAR(100),
# 				assist VARCHAR(100))''')

cursor.execute("INSERT INTO callod (kills,death,assist) VALUES(?,?,?)", (kills, death, asist))
conn.commit()

conn.close()