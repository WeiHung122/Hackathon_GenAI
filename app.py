from flask import Flask, request, jsonify
from flask_cors import CORS
from model import train_process, test_process

app = Flask(__name__)
CORS(app)

import boto3
s3 = boto3.client(
    's3',
    aws_access_key_id='',
    aws_secret_access_key=''
)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello from EC2!")
    
@app.route('/train', methods=['GET'])
def train():
    train_process()
    return {"message": "Finish"}

@app.route('/inference', methods=['GET'])
def inference():
    test_process()
    return {"message": "Finish"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)