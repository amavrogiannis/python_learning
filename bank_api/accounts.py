""" Account API """

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    
    def post(self, account_id: int, balance: int) -> None:
        self.account_id = account_id
        self.balance = balance

    def get(self, account_id: int, balance: int):
        self.account_id = post.account_id
        self.balance = post.balance

@app.route('/hello_this')
def this_basic():
    return {'data': 'Hello Function'}

def this_second(use_this: str):
    print(f'I am using {use_this}')

api.add_resource(Hello, "/hello")

if __name__ == "__main__":
    app.run(debug=True)