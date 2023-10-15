""" Account API """

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    ''' This is an example hello world '''
    def get(self):
        return { 'data':'This is class' }

class Advance(Resource):
    ''' New little more complex '''
    def get(self, name, age):
        return {'message': f'name: {name} and age: {age}'}

''' Calling the Flask app using /hello_this path '''
@app.route('/hello_this')
def this_basic():
    return {'data': 'Hello Function'}

''' Second route, which calls /this/<custom string> and returns '''
@app.route('/this/<use_this>')
def this_second(use_this):
    return f'I am using {use_this}'

''' Calling Hello class '''
api.add_resource(Hello, "/hello")

''' Calling advanced API '''
api.add_resource(Advance, "/user/<string:name>/<int:age>")

if __name__ == "__main__":
    app.run(debug=True)


""" 
Use the Instruction manual (MEDIUM) to understand the building of an API 
https://rajansahu713.medium.com/hands-on-guide-to-restful-api-using-flask-python-16270f866ffe

"""