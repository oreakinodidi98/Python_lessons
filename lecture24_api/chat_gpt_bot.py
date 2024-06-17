import requests
# library to make HTTP requests, allows you to send HTTP requests using Python

url = "https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions"
# the URL of the API endpoint
query = "which one is better django or flask?"

payload = {
	"model": "gpt-3.5-turbo",
	"messages": [
		{
			"role": "user",
			"content": query
		}
	]
}
# payload is the data that you want to send to the API endpoint, so the body

headers = {
	"x-rapidapi-key": "feebb649f6mshbd065a7b283c4abp1eaabbjsn8ccbd6753d10",
	"x-rapidapi-host": "chatgpt-best-price.p.rapidapi.com",
	"Content-Type": "application/json"
}
# headers are the metadata that you want to send to the API endpoint, so the header

response = requests.post(url, json=payload, headers=headers, timeout=10)

print(response.json())
# print the response from the API endpoint, to get only the message content
print(response.json()["choices"][0]["message"]["content"])