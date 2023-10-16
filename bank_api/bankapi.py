# pylint: disable=R0903, E0401
"""
Bank account API
"""
import json
from time import gmtime, strftime
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from account import BankAccount

# """ Flask Env Variable """
app = Flask(__name__)
api = Api(app)

file = "accounts.json"

gmt_time = strftime("%d/%m/%Y %H:%M:%S", gmtime())

class AccountID(Resource):
    """ API Class for Bank Account """

    def get(self, account_no:int):
        """ Applying AccountID and Balance """
        with open(file, 'r') as bank_file: 
            transactions_data = json.load(bank_file)


        for items in transactions_data:
            if 'account_id' in items and items['account_id'] == account_no:
                results = app.response_class(
                    response=json.dumps(items, indent=4),
                    status=200,
                    mimetype='application/json'
                )

        return results
    
class Deposit(Resource):
    def post(self, account_no:int, amount:int):
        with open(file, 'r') as deposit:
            data = json.load(deposit)
        
        for item in data:
            if "transactions" in item and isinstance(item["transactions"], list):
                for transaction_item in item["transactions"]:
                    if "balance" in transaction_item and transaction_item["find"] != None:
                        new_balance = transaction_item["balance"] + amount
                        transaction_item["time"] = f'{gmt_time}'
                        transaction_item["amount"] = f'{amount}'
                        transaction_item["balance"] = f'{new_balance}'

        with open('your_file.json', 'w') as f:
            json.dump(data, f, indent=4)
        
        results = app.response_class(
            response={'message':f'Deposited {amount} to {account_no}'},
            status=200,
            mimetype='application/json'
        )


# Endpoint 1 
api.add_resource(AccountID, "/account/<int:account_no>", endpoint= "account")
# copy: http://127.0.0.1:5000/account/1002

# Endpoint 2
api.add_resource(Deposit, "/account/<int:account_no>/deposit/<int:amount>", endpoint= "deposit")
# copy: http://127.0.0.1:5000/account/1002/deposit/100

if __name__ == "__main__":
    app.run(debug=True)

# End-of-file (EOF)
