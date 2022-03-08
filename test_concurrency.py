import requests
import sys 

for i in range(int(sys.argv[1])):
    requests.post('http://127.0.0.1:5000/', headers={'accept': 'application/json'})
