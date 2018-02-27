from flask import Flask, send_file
import socket
import os, random
app = Flask(__name__)

@app.route('/send_panda', methods=['GET'])
def send_panda():
	return random.choice(os.listdir("/resources"))

if __name__ == '__main__':
	ip = socket.gethostbyname(socket.gethostname())
	app.run(host=ip, port=80)
