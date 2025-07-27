import time
import random

def main():
    for tries in range(1,5):
        try:
            num = random.random()
            if num < 0.5:
                print(f'Success {num}')
                return
            raise ConnectionError('Network Issue')
        except:
            delay = tries ** 2
            print(f'Retrying after {delay}s')
            time.sleep(delay)
    print("Operation failed after retries.")

main()