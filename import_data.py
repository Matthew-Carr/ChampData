import json
import urllib2
from ChampData.models import Champion

url = 'https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?champData=stats&api_key=7f057410-5d0b-4174-b2e4-ad93f77c18d6'
current_champions = [x.name for x in Champion.objects.all()]
#print (current_champions)

data = json.loads(urllib2.urlopen(url).read())

for champion in data["data"]:
	if data["data"][champion]["name"] not in current_champions:
		new = Champion(name = data["data"][champion]["name"],
						hp = data["data"][champion]["stats"]["hp"],
						hpPlus = data["data"][champion]["stats"]["hpperlevel"],
						hp5 = data["data"][champion]["stats"]["hpregen"],
						hp5Plus = data["data"][champion]["stats"]["hpregenperlevel"],
						mp = data["data"][champion]["stats"]["mp"],
						mpPlus = data["data"][champion]["stats"]["mpperlevel"],
						mp5 = data["data"][champion]["stats"]["mpregen"],
						mp5Plus = data["data"][champion]["stats"]["mpregenperlevel"],
						ad = data["data"][champion]["stats"]["attackdamage"],
						adPlus = data["data"][champion]["stats"]["attackdamageperlevel"],
						asPlus = data["data"][champion]["stats"]["attackspeedperlevel"],
						ar = data["data"][champion]["stats"]["armor"],
						arPlus = data["data"][champion]["stats"]["armorperlevel"],
						mr = data["data"][champion]["stats"]["spellblock"],
						mrPlus = data["data"][champion]["stats"]["spellblockperlevel"],
						ms = data["data"][champion]["stats"]["movespeed"],
						adRange = data["data"][champion]["stats"]["attackrange"]
						)
		new.save()



