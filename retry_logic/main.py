import requests
from urllib3.exceptions import ProtocolError
import time
import random

# url = 'http://localhost:8080/status/100,200,300,400,500'
url = 'https://httpbin.org/status/100,200,300,400,500'

def get_response(url) -> int:
    res = requests.get(url)
    return res.status_code

def backoff_fn(test_url,max_tries = 10):
    for trial in range(1,max_tries+1):
        try:
            response = get_response(test_url)
            if response == 200:
                return f'Success {response}'
            else:
                raise ValueError(f"{response}")        
        except (requests.RequestException, ProtocolError, ValueError) as e:
            delay = random.randint(1,5)
            print(f'Trial {trial}: {e} — Retrying after {delay}s...')
            time.sleep(delay)

    return "Failed after {} trials".format(max_tries)

print(backoff_fn(url))