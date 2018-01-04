from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Hello world'

@app.route('/headers')
def headers():
  return "{}".format(request.headers)

@app.route('/ip')
def ip():
  app.logger.debug("Request remote addr %s",  request.remote_addr)
  app.logger.debug("Request X-Forwarded-For %s", request.headers.get('X-Forwarded-For', 'empty'))
  return request.headers.get('X-Forwarded-For', request.remote_addr)

if __name__ == '__main__':
  app.run(host='::', port=8080)
