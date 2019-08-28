from flask import Flask
from flask_restplus import Resource, Api, fields
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app,
          version='0.1',
          title='c7w写的破程序',
          description='c7w写的破API'
)

@api.route('/hello_world')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@api.route('/')
class Hello(Resource):
    def get(self):
        return "this"

if __name__ == '__main__':
    app.run(debug=True)