from flask import Flask
from flask import request
import socket
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
	ip = socket.gethostbyname(socket.gethostname())
	app.run(host=ip, port=80)
        
