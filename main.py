from flask import Flask, request, jsonify
from replit import db
import random

app = Flask('app')

@app.route('/')
def hello_world():
  return '<img src = "https://wildaware.s3.ap-south-1.amazonaws.com/image39.jpg">'

@app.route('/input', methods = ['GET'])
def input():
  temp = random.randint(0, 1000)
  aname = request.args.get('aname')
  loc = request.args.get('loc')
  desc = request.args.get('desc')
  info = [aname, loc, desc]
  db[str(temp)] = info
  return jsonify(info)

@app.route('/output', methods = ['GET'])
def output():
  output = []
  dict = {}
  for i in db:
    aname = db[i][0]
    loc = db[i][1]
    desc = db[i][2]
    dict = {
      "aname": aname,
      "loc": loc,
      "desc": desc
    }
    output.append(dict)
  print(output)
  return jsonify(output)

app.run(host='0.0.0.0', port=8080)
