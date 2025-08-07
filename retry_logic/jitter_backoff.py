import time
import random
import requests

class InvalidReturnCodeError(Exception):
    def __init__(self, value):
        super().__init__(f"Invalid return code: {value}")
        self.value = value

def get_response(url) -> int:
    try:
        res = requests.get(url)
        return res.status_code
    except requests.exceptions.ConnectionError:
        return 100 

def backoff_with_jitter(test_url,base_delay = 1,max_attempts = 5):
    for attempt in range(1,max_attempts + 1):
        try:
            response = get_response(test_url)

            if response == 200:
                return 200
            else:
                raise InvalidReturnCodeError(response)
                 
        except InvalidReturnCodeError as e:
            delay = base_delay + random.uniform(0, 3) # simple jitter
            print(f'Trial {attempt}: {e} — Retrying after {delay}s...')
            time.sleep(delay)

    return "Failed after {} trials".format(max_attempts)


if __name__ == '__main__':
    url = 'http://localhost:8080/status/100,200,300,400,500'
    # url = 'https://httpbin.org/status/100,200,300,400,500'

    result = backoff_with_jitter(url)
    if result == 200:
        print('✅ Success')
