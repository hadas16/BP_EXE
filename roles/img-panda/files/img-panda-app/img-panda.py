from flask import Flask, send_file
import os, random
app = Flask(__name__)

@app.route('/send_panda', methods=['GET'])
def send_panda():
	return random.choice(os.listdir("/resources"))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
