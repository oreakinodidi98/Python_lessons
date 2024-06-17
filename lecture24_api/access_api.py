import requests

url = "http://127.0.0.1:5000/api/v1"
# the URL of the API endpoint

headers = {
    "Content-Type": "application/json",
    "charset": "utf-8"
}
# headers are the metadata that you want to send to the API endpoint, so the header
params = {
    "name": "Ore"
}
# payload is the data that you want to send to the API endpoint, so the body
response = requests.get(url, headers=headers, data=params , timeout=10)

print(response.json()) # output <Response [200]>