# API (Application Programming Interface)

- interface that provides a set of functions to the user
- where the underlying mechanism of that function is hidden.
- Web API: It is an API that travels through the internet. Usually called client-server architecture
  - interaction between the client, internet and server
  
## API terminologies

- **Integration**: API integration refers to the process of connecting two or more applications or systems by using APIs (Application Programming Interfaces) to exchange data and perform actions.
- **Call**: The process of sending a request to your API after setting up the right endpoints
- **Monetization**: API monetization is a process by which a business can create revenue from its APIs.

## HTTP

- HTTP : HyperText Transfer Protocol
- when you make a request to website 
- you have : protocol -> URL->Parameters-> query of that particular thing
- 200 = everything went well
- 400- error from client side -> so my side
- 500 = error on server side

## payload

- XML
- .JSON

## Rest

- Representational state transfer
- protocal that will allow connection between the client and server over the internet
- URI = uniform resource identifier
- Endpoint
- Method
  - POST(Create), GET(retrieve), PUT (Update), DELETE
- Header
- Body -> pay load -> Part that will carry your information over the internet

### Example

- set up postman in VS code
- - rapidapi.com
  - to get api that you need
  - subscribe to api
- E.G. chatgpt-best-price
  - use python
  - client : request
set URL as POST
body -> Raw _> JSON -> add payload
Header -> add keys

```py
```

## API Types

- Private
  - people are paying for it to be used
  - belong to companies
  - employes can use it but outsiders cant
- Partner
  - e.g. spotify
  - employee has access to all API
  - validated user can also connect to it
  - need authurisation for certain features
- Public
  - eveyone is able to use it
  - no authentication or authorisation required
  - limits

## Flask VS Django

- database: Django has its own one, Flask = SQL Alchemy
- Desighn: Flask = minimal
- API integration: Flask = built in
- rapidapi.com
  - to get api that you need

## Flask

- import flask
- app = Flask(__name__)
- if __name__ == '__main__':
    app.run(debug=True)
- to run flask 

```py
from flask import Flask, request, jsonify

app = Flask(__name__)

# run server
if __name__ == '__main__':
    app.run(debug=True)
```

- can put url in postman and run