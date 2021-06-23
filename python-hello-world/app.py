from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route('/')
def index():
    app.logger.info('Main request succesfull')
    return 'Hello world'

@app.route('/status')
def status():
    response = app.response_class(
        json.dumps({'Result': 'Ok-healthy'}),
        status = 200,
        mimetype = 'application/json'
    )
    app.logger.info('Status request succesfull')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
        json.dumps({ 'data': { 'UserCount': 120, 'UserActive': 23 } }),
        status = 200,
        mimetype = 'application/json' 
    )
    app.logger.info('Metrics request succesfull!')
    return response 

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')