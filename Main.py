from flask import Flask, render_template
import os
import sys
from flask import request
from random import randint
from flask_cors import CORS
import json
from flask import make_response
from flask import Flask, Response, abort

JSON_MIME_TYPE = 'application/json'

app = Flask(__name__)
CORS(app) #this will enable all (free - world)
'''
    more CORS
    https://flask-cors.readthedocs.io/en/latest/
'''

def success_json(data):
    content = json.dumps(data)
    return content, 200, {'Content-Type': JSON_MIME_TYPE}

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/test")
def test():
  return "Hello, cross-origin-world!" 

'''
    /test/add?a=2&b=2
    http://127.0.0.1:5000/add?a=2&b=2
'''
@app.route('/add')
def add():   
    
    ''' # this will not work for POST method. This is only for GET method
    a = request.args.get('a', type=int, default=49)
    b = request.args.get('b', type=int, default=78) 
    '''
    
    a = request.form.get('a', type=int, default=49)
    b = request.form.get('b', type=int, default=487)
    
    
    c = a + b

    result_json = {
        'result': c,
        
        'api_error': 0
    }
    
    return success_json(result_json)


if __name__ == '__main__':
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    
    app.run(host= host, port = port, use_reloader = False)
    

    
'''
Sources:
    https://flask-cors.readthedocs.io/en/latest/   
'''