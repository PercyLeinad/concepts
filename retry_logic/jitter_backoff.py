import time
import random
from urllib3.exceptions import ProtocolError
import requests

url = 'http://localhost:8080/status/100,200,300,400,500'
# url = 'https://httpbin.org/status/100,200,300,400,500'

def get_response(url) -> int:
    res = requests.get(url)
    return res.status_code

def backoff_with_jitter(test_url,base_delay = 1,max_attempts = 8):
    for attempt in range(max_attempts):
        try:
            response = get_response(test_url)
            if response == 200:
                return f'Success {response}'
            else:
                raise ValueError(f"{response}")        
        except (requests.RequestException, ProtocolError, ValueError) as e:
            delay = base_delay + random.uniform(0, 1)
            print(f'Trial {attempt}: {e} — Retrying after {delay}s...')
            time.sleep(delay)

    return "Failed after {} trials".format(max_attempts)

print(backoff_with_jitter(url,))