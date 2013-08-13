from flask import (
    Flask,
    url_for,
    request,
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
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'


@app.route('/echo', methods=HTTP_VERBS)
def api_echo():
    def echo_request_method(method):
        return 'ECHO: %s\n' % method

    if request.method in HTTP_VERBS:
        return echo_request_method(request.method)


if __name__ == '__main__':
    app.run()
