from flask import (
    Flask,
    url_for,
    request,
    json,
    jsonify,
)

app = Flask(__name__)
HTTP_VERBS = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE']


@app.route('/')
def app_root():
    return 'Welcome'


@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')


@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid


@app.route('/hello')
def api_hello():
    data = {
        'hello': 'world',
        'number': '3',
    }
    resp = jsonify(data)
    resp.status_code = 200

    return resp


@app.route('/echo', methods=HTTP_VERBS)
def api_echo():
    def echo_request_method(method):
        return 'ECHO: %s\n' % method

    if request.method in HTTP_VERBS:
        return echo_request_method(request.method)


@app.route('/messages', methods=HTTP_VERBS[1:2])
def api_message():
    if request.headers['Content-Type'] == 'text/plain':
        return 'Text Message: ' + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return 'JSON Message: ' + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return 'Binary message written!'
    else:
        return '415 Unsupported Media Type ;)'


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


@app.route('/users/<userid>', methods=HTTP_VERBS[0:1])
def api_users(userid):
    users = {
        '1': 'John',
        '2': 'Steve',
        '3': 'Bill',
    }

    if userid in users:
        return jsonify({userid: users[userid]})
    else:
        return not_found()

if __name__ == '__main__':
    app.run()
