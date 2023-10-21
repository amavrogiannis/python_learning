from fastapi import Response
from time import gmtime, strftime
import json

gmt_time = strftime("%d/%m/%Y %H:%M:%S", gmtime())


def open_file(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data


def save_changes(file, data):
    with open(file, 'w') as f:
        output = json.dump(data,f, indent=4)
    return output


def deposit_service(account_no, amount, file):
    data = open_file(file)

    for account in data:
        if account['account_id'] == account_no:
            account['balance'] += amount
            transaction = {
                'time': gmt_time,
                'amount':  amount,
                'balance': account['balance']
            }

            account['transactions'].append(transaction)
            break
    
    save_changes(file, data)


def out_results(account_no, file):
    with open(file, 'r') as f:
        data = json.load(f)

    for account in data:
        if account['account_id'] == account_no:
            results = Response(
                content=json.dumps(account, indent=4),
                media_type='application/json'
            )
            results.status_code = 200
    
    return results

