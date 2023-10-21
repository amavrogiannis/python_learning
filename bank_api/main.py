from fastapi import FastAPI, Response
from time import gmtime, strftime
from services import account, deposit, withdraw
import uvicorn
import json

gmt_time = strftime("%d/%m/%Y %H:%M:%S", gmtime())

app = FastAPI()

file = '/Users/amavrogiannis/Dev_Docs/Git/python_learning/bank_api/accounts.json'

@app.get('/')
def this():
    return {'message' : 'welcome to alex\'s bank'}

# i.e. URL /account/<account_id>
@app.get('/account/{account_no}')
def account_service(account_no:int):
    result = account.bank_account(account_no, file)
    return result

# i.e. URL /account/<account_id>/deposit/<amount>
@app.get('/account/{account_no}/deposit/{amount}')
def deposit_service(account_no:int, amount:int):
    if 0 > amount:
        return {'message':'Cannot deposit less than 0'}
    else:
        deposit.deposit_service(account_no, amount, file)

        json_this = {
            'message':f'You deposited {amount} to {account_no} account',
            'to view':f'http://127.0.0.1:8000/account/{account_no}'
            }
        message = Response(
            content=json.dumps(json_this, indent=4),
            media_type='application/json'
        )
        message.status_code = 200

        return message

# i.e. URL /account/<account_id>/withdraw/<amount>
@app.get('/account/{account_no}/withdraw/{amount}')
def withdraw_service(account_no:int, amount:int):
    if 0 > amount:
        return {'message':'Cannot withdraw less than 0'}
    else:
        withdraw.withdraw_service(account_no, amount, file)

        json_this = {
            'message':f'You withdrawn {amount} to {account_no} account',
            'to view':f'http://127.0.0.1:8000/account/{account_no}'
            }
        message = Response(
            content=json.dumps(json_this, indent=4),
            media_type='application/json'
        )
        message.status_code = 200

        return message


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True)