from flask import Flask

#Creating a New Flask App Instance
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'