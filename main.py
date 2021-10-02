from flask import Flask, request, jsonify
from replit import db
import random

app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/input', methods = ['GET'])
def input():
  temp = random.randint(0, 1000)
  aname = request.args.get('aname')
  loc = request.args.get('loc')
  desc = request.args.get('desc')
  info = [aname, loc, desc]
  db[str(temp)] = info
  return jsonify(info)

app.run(host='0.0.0.0', port=8080)
