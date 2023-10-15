# pylint: disable=R0903, E0401
"""
Bank account API
"""
import json
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from account import BankAccount

# """ Flask Env Variable """
app = Flask(__name__)
api = Api(app)

class AccountID(Resource):
    """ API Class for Bank Account """

    def get(self, account_id:int, balance:int=1200):
        """ Applying AccountID and Balance """
        data = BankAccount(account_id, balance)
        data.account_id = account_id
        data.balance = balance
        self.transactions =[]
        json_list = json.dump(self.transactions)
        return {
            'account_id': f'{data.account_id}',
            'balance': f'{data.balance}',
            'transactions': f[{json_list}]
        }

    # def post(self):
    #     bank = BankAccount()
    #     """ This method will update the JSON file """
    #     data = request.get_json()
    #     deposit = data['deposit']
    #     balance = bank.deposit(deposit)

    #     return {
    #         'deposit': f'{deposit}'
    #     }

# Endpoint 1 
api.add_resource(AccountID, "/account/<int:account_id>", endpoint= "account")
# copy: http://127.0.0.1:5000/account/1002

# Endpoint 2
# api.add_resource(AccountID, "/account/<int:account_id>/deposit/<int:ammount>", endpoint= "deposit")
# copy: http://127.0.0.1:5000/account/1002/deposit/100

if __name__ == "__main__":
    app.run(debug=True)

# End-of-file (EOF)
