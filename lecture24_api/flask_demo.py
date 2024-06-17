from flask import Flask, request, jsonify

app = Flask(__name__)

# create a route
# this is my API endpoint
@app.route('/', methods=['POST', 'GET']) # define a route for the API endpoint, that accepts POST and GET requests
def hello_world():# define hello_world function that returns a string
    return 'Hello, World!'

@app.route('/api/v1/', methods=['POST']) # Define a route for the endpoint '/api/greet' that accepts POST requests
def greet(): # Define the greet function to handle the POST requests to the '/api/greet' endpoint
    data = request.get_json() # Retrieve the JSON data sent in the request
    name = data.get('name', 'default') # Retrieve the value of the 'name' key in the JSON data, if it does not exist, return 'default'
    return f"Hello, {name}!"
    #return jsonify({'message': f'Hello, {name}!'})

# run server
if __name__ == '__main__':
    app.run(debug=True)