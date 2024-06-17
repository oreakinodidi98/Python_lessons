import requests

url = "https://spotify23.p.rapidapi.com/search/"

querystring = {"q":"drake","type":"multi","offset":"0","limit":"10","numberOfTopResults":"5"}

headers = {
	"x-rapidapi-key": "feebb649f6mshbd065a7b283c4abp1eaabbjsn8ccbd6753d10",
	"x-rapidapi-host": "spotify23.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())