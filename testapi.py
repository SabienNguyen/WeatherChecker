import requests

url = "https://visual-crossing-weather.p.rapidapi.com/forecast"

querystring = {"aggregateHours":"24","location":"Riverside,CA,USA","contentType":"json","unitGroup":"us","shortColumnNames":"0"}

headers = {
	"X-RapidAPI-Key": "efe9af46b8msh4739e0845e52ecap159470jsn1066ec38a62a",
	"X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)