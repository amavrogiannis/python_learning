from fastapi import Response
import json

def bank_account(account_no, file):
    """ Applying AccountID, Balance and Transactions """
    with open(file, 'r') as bank_file: 
        transactions_data = json.load(bank_file)


    for items in transactions_data:
        if 'account_id' in items and items['account_id'] == account_no:
            results = Response(
                content=json.dumps(items, indent=4),
                media_type='application/json'
            )
            results.status_code = 200

    return results