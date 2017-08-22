import pymongo
from bottle import route, run


@route('/')
def index():
    conn = pymongo.MongoClient('localhost')
    db = conn.test
    item = db.names.find_one()

    return '<b>Hello %s!</b>' % item['name']


run(host='localhost', port=8080)
