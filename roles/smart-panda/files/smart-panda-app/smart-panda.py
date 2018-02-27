from flask import Flask
from flask import request
import os

num_of_post_req = 0 

app = Flask(__name__)


@app.route('/smartpanda', methods=['GET', 'POST'])

def smartpanda():
	global num_of_post_req
	if request.method == 'GET':
	    return str(num_of_post_req)
	if request.method == 'POST':
	    num_of_post_req = num_of_post_req + 1
            return None

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
        
