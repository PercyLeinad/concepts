import requests
import time
import random

class InvalidReturnCodeError(Exception):
    def __init__(self, value):
        super().__init__(f"Invalid return code: {value}")
        self.value = value

def get_response(url) -> int:
    try:
        res = requests.get(url)
        return res.status_code
    except requests.exceptions.ConnectionError:
        return 100  # Return a sentinel value

def backoff_fn(test_url, max_tries=10):
    for trial in range(1, max_tries + 1):
        try:
            response = get_response(test_url)

            if response == 200:
                return response

            # Raise custom exception for specific invalid codes
            if response in {100, 300, 400, 500}:
                raise InvalidReturnCodeError(response)

            # Catch-all for other non-200 codes
            raise Exception(f"Unexpected status code: {response}")

        except InvalidReturnCodeError as e:
            print(f"Trial {trial} — {e}. Retrying...")
        except Exception as e:
            print(f"Trial {trial} — {e}. Retrying...")

        delay = random.randint(1, 5)
        time.sleep(delay)

    print(f"Failed after {max_tries} trials.")

if __name__ == '__main__':
    url = 'http://localhost:8080/status/100,200,300,400,500'
    # url = 'https://httpbin.org/status/100,200,300,400,500'
    
    result = backoff_fn(url)
    if result == 200:
        print('✅ Success')
