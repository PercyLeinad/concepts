import time
import random

def exponential_backoff(retries=5, base_delay=1, max_delay=16):
    for i in range(retries):
        try:
            if random.random() < 0.7:
                raise ConnectionError("Network issue")
            print("Operation succeeded!")
            return
        except ConnectionError as e:
            delay = min(max_delay, base_delay * (2 ** i))
            print(f"{e} - retrying in {delay}s...")
            time.sleep(delay)
    print("Operation failed after retries.")

if __name__ == "__main__":
    exponential_backoff()
