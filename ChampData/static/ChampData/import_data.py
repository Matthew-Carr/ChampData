import json
import urllib2
from models import champion

url = 'https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?champData=stats&api_key=7f057410-5d0b-4174-b2e4-ad93f77c18d6'

data = json.loads(urllib2.urlopen(url).read())

for champion in data["data"]:
	if champion == "Aatrox":
		print(data["data"]["Aatrox"]["stats"]["attackrange"])


