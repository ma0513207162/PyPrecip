import requests
from requests.exceptions import Timeout, RequestException 
from .exwarn import raise_exception, raise_warning 


def send_request(URL: str, PARAMS: dict):
    MAX_RETRIES = 3     # 最大重试次数 
    retry_count = 0     

    while retry_count < MAX_RETRIES:
        try:
            response = requests.get(URL, params = PARAMS, timeout = 10)
            if response.status_code == 200: return response
        except Timeout:
            retry_count += 1 
            print(f"Request timed out, retrying... (Attempt {retry_count}/{MAX_RETRIES})")
        except RequestException as e:
            raise_exception(f"An error occurred: {e}", RequestException)
    else:
        raise_exception("Maximum number of retries reached, giving up.", RequestException)

