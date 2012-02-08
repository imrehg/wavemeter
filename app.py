import os

from bottle import route, run

@route('/hello/:name')
def index(name='World'):
    return '<b>Hello %s!</b>' % name

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    run(host='0.0.0.0', port=port)
