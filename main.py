from flask import Flask, request, jsonify
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/input', methods = ['GET'])
def input():
  aname = request.args.get('aname')
  loc = request.args.get('loc')
  desc = request.args.get('desc')
  info = [aname, loc, desc]
  return jsonify(info)

app.run(host='0.0.0.0', port=8080)