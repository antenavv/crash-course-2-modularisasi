"""
cara nge-print tanpa response :

import requests

url = 'https://detik.com'
try:
    requests.get(url)
    print('Success!')
except Exception as e:
    print ('There is an error', e)
print('Program ended')
"""
"""
cara nge-print dengan response :

import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    print(f'Success!{response}')
except Exception as e:
    print (f'There is an error {e}')
print('Program ended')
"""

import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success! Response = {response.status_code}')
        print (f'content {response.text}')
    else:
        print (f'Woops, ada kesalahan request {response.status_code}')
except Exception as e:
    print (f'There is an error {e}')
print('Program ended!')

