import os
from dotenv import load_dotenv
import requests

load_dotenv()

sk = os.environ.get("secret")


def account_number(acct_num, bank_code):
    url = f'https://api.paystack.co/bank/resolve?account_number={acct_num}&bank_code={bank_code}'
    
    headers = {
        "Authorization": f"Bearer {sk}",
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json() 
        return data
    return response
    
def bank_code():
    url = "https://api.paystack.co/bank"
    
    headers = {
        "Authorization": f"Bearer {sk}",
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()['data']
        for bank_info in data:
            print(bank_info['name'], bank_info['code'])
        
# print(bank_code())
print(account_number(354435677, "011" ))
     