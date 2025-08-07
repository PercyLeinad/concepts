#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Demo of built in retry
from termcolor import cprint
import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import urllib3

urllib3.disable_warnings(InsecureRequestWarning)

retry_strategy = Retry(
    backoff_factor=1,
    total=3,
    status_forcelist=[100, 300, 400, 500],
    backoff_jitter=0.5
)

adapter = HTTPAdapter(max_retries=retry_strategy)

def create_session():
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Python Exploit Tool)'
    })
    session.verify = False
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session

def normalize_url(url: str) -> str:
    return url if url.startswith(('http://', 'https://')) else "https://" + url


def main(URL):
    session = create_session()
    normalized_url = normalize_url(URL)
    try:
        res = session.get(normalized_url)
        return res.status_code
    except requests.exceptions.RetryError as e:
        return 'Max retries'
    except requests.exceptions.ConnectionError as e:
        return 'Connection Error' 
    except requests.exceptions.HTTPError as e:
        return 'Http Error'
    # except requests.exceptions.RequestException as e:
    #     cprint(f"General request exception: {e}", color='red')

url = 'http://localhost:8080/status/200,300,400,100,500'

result = main(url)

if result == 200:
    cprint('Lucky','blue')
else:
    cprint(f'Request failed! {result}',color='red')

if __name__ == '__main__':
    url = 'http://localhost:8080/status/200,300,400,100,500'
    main(url)