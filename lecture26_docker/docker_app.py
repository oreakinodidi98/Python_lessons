from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST' ])
def hello_world():
    return {"msg": "Hello, World!"}

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
    # the debug=True argument enables debugging mode, which helps in identifying and fixing errors in the code