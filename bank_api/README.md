# Bank API Challenge.

Using flask, build an API for external systems to access and modifty customer account data. Sample data is provided in the file `accounts.json`.

`accounts.json` 
The file contians the following data:
`account_id` : this is a unqiue customer ID.
`balance`: a float representing the customers avaialable balance. This cannot go below £0.
`transactions`: a list of previous transactions. Each item contains the time and date, amount deposited or withdraw and the balance after that transaction.

## Requirements:
- [x] endpoint requirement 1: `/account/<account_id>` will give all of the data from `accounts.json` for that account. (account_id, balance, transactions)
- [x] endpoint requirement 2: `/account/<account_id>/deposit/<amount>` will allow the API consumer to deposit money into that account, altering the balance.
    - sub requirement: this should appear as a new transaction in the accounts transaction list and be saved to the json file.
- [x] endpoint requirement 2: `/account/<account_id>/withdraw/<amount>` will allow the API consumer to withdraw money from that account, altering the balance.
    - sub requirement: this should appear as a new transaction in the accounts transaction list and be saved to the json file.
- [ ] If the user requests an account that does not exist, the api should return an error message.
- [x] If the user tries to deposit £0 or less, the api should return an error message.
- [x] If the user tries to withdraw more than the accounts balance , the api should return an error message.
- [x] Access should be through localhost (127.0.0.1) port 5000. *I used FastAPI therefore will be 8000. It can chance to port 5000.*
- [x] No tests required. 