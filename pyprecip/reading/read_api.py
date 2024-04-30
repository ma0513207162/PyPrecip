import requests, json
from requests.exceptions import Timeout, RequestException 


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


def get_area_code(area_name: str = ""):
    """
    with open("./static/constant.json", "r", encoding="utf-8") as file:
        READ_API_DATA: dict = json.load(file)["READ_API"]    
    DUP_PLACE_NAMES = READ_API_DATA["DUP_PLACE_NAMES"]
    """

    if area_name != "":
        with open("./static/city_code.json", "r", encoding="utf-8") as file:
            city_code_table: dict = json.load(file)
        try:
            area_code = city_code_table[area_name] 
            if isinstance(area_code, list):  return area_code
            else: return int(area_code) 
        except KeyError:
            # city_code_keys = city_code_table.keys() 
            raise_exception(f"There is no city with the status of {area_name}.", KeyError)
    else:
        raise_exception("area_name parameter cannot be null or invalid.", ValueError) 


def get_weather_data(area_code: int = -1, area_name: str = "", forecasts: bool = False) -> dict:
    if not isinstance(area_code, int):
        raise_exception("area_code parameter must be of type int.", TypeError)
    if not isinstance(area_name, str):
        raise_exception("area_name parameter must be of type str.", TypeError)
    if not isinstance(forecasts, bool): 
        raise_exception("forecasts parameter must be of type bool.", TypeError)
            
    request_result: dict = {}
    with open("./static/constant.json", "r", encoding="utf-8") as file:
        READ_API_DATA: dict = json.load(file)["READ_API"]    

    # 自动获取当前位置、根据地名获取区域编码 
    if area_code == -1 and area_name == "":
        # 自动获取当前的位置 
        URL: str = READ_API_DATA["LOCATION_URL"]
        PARAMS: dict = { "key": READ_API_DATA["WEATHER_KEY"] }

        # 发送 request 请求 
        response = send_request(URL, PARAMS)            
        location_data: dict = response.json()

        if location_data["status"] == '1' and location_data["infocode"] == "10000":
            area_code = location_data["adcode"]
            request_result["area_code"] = location_data["adcode"]
        else:
            raise_exception("An unknown error occurred with the ip location request. Please try again later", RequestException)
    elif area_code == -1 and area_name != "": 
        get_result = get_area_code(area_name)
        if isinstance(get_result, list):  
            raise_warning(f"The place name has multiple regional codes:{get_result},the first one is selected by default.")
            area_code = get_result[0] 
        else: 
            area_code = get_result
        request_result["area_code"] = area_code
    else:
        if area_name != "": 
            raise_warning("The area_code parameter overrides the effect of the area_name parameter.")
        request_result["area_code"] = area_code

    # 请求实时/未来的气候数据 
    WEATHER_URL = READ_API_DATA["WEATHER_URL"]
    WEATHER_KEY = READ_API_DATA["WEATHER_KEY"]
    ext_type = "base" if forecasts == False else "all" 
    WEA_PARAMS = {"city": area_code,  "key": WEATHER_KEY, "extensions": ext_type}
        
    # 发送 http 请求
    response = send_request(WEATHER_URL, WEA_PARAMS)            
    weather_data = response.json()

    if weather_data["status"] == '1' and weather_data["infocode"] == '10000':
        if forecasts: 
            forecasts_or_lives = weather_data["forecasts"][0]
        else:
            forecasts_or_lives = weather_data["lives"][0]
            forecasts_or_lives_copy = forecasts_or_lives.copy()
            for key in ["province", "city", "reporttime", "adcode"]:
                del forecasts_or_lives_copy[key]
            forecasts_or_lives["casts"] = [forecasts_or_lives_copy]

        request_result["province"] = forecasts_or_lives["province"]
        request_result["city"] = forecasts_or_lives["city"]
        request_result["update_time"] = forecasts_or_lives["reporttime"] 
        request_result["casts"] = forecasts_or_lives["casts"]
        
        return request_result                    
    else:
        raise_exception("An unknown error occurred in the climate data request. Please try again later", RequestException)





if __name__ == "__main__":
    from utils.exception_ import CustomException 

    exc = CustomException()  
    print(exc)