import json
from requests.exceptions import RequestException 
from ..utits.http_ import send_request 
from ..utits.sundries import check_param_type
from ..utits.except_ import RaiseException as exc 
from ..utits.warn_ import RaiseWarn as warn

WEATHER_KEY = "123"


def __check_weather_key(func):
    def wrapper(*args, **kwargs):
        """
        Check whether the global variable WEATHER_KEY is empty, and if it is, 
        prompt the user to register a Web service API and assign a value.
        """
        if not WEATHER_KEY:
            print("\033[93m- PyPrecip Warning: \033[0mWEATHER_KEY is not set.")
            print("\033[0m- Please register for a Web Service API at\033[94m https://console.amap.com/dev/key/app.")
            print("\033[0m- After registering, set the value of the global variable 'read_api.WEATHER_KEY' like this:")
            print("\033[92m- read_api.WEATHER_KEY = 'your_api_key_here' \033[0m")
            return; 
        return func(*args, **kwargs)
    return wrapper


@__check_weather_key
def get_address_info(address: str = "", city: str = None) -> dict:
    """
    The Amap geocoding service API is encapsulated to obtain the region code based on the provided address information.

    Parameters
    ------------------------------
    - address (str): The address information to obtain the corresponding region code
    - city (str): The city name, used to assist in obtaining the region code based on the address

    
    Returns
    -------------------------------
    - dict: A dictionary containing the region code information based on the provided address
    - If the address parameter is empty or invalid, a ValueError exception is raised
    - If an error occurs during the request, a RequestException is raised
    """

    check_param_type(address, str, "address"); 
    check_param_type(city, str, "city")

    if address != "":
        with open("./pyprecip/_constant.json", "r", encoding="utf-8") as file:
            READ_API_DATA: dict = json.load(file)["READ_API"]    
        
        GEOCODING_URL: str = READ_API_DATA["GEOCODING_URL"]
        PARAMS: dict = { 
            "key": WEATHER_KEY, 
            "address": address,  "city": city
        }

        # 发送 request 请求 
        response = send_request(GEOCODING_URL, PARAMS)   
        address_info: dict = response.json()

        if address_info["status"] == "1" and address_info["infocode"] == "10000":
            if int(address_info["count"]) > 1:
                warn.raise_warning(f"The place name has multiple regional codes: {address}, the first one is selected by default.")
            return address_info
        else:
            except_address_info: str = address_info["info"]; 
            exc.raise_exception(f"An unknown error occurred in the address request. {except_address_info} \
                             Please try again later", RequestException)
    else:
        exc.raise_exception("address parameter cannot be null or invalid.", ValueError) 


@__check_weather_key
def get_weather_data(area_code: int = -1, address: str = "", 
                     city: str = "", forecasts: bool = False) -> dict:
    """
    The Amap Open Platform weather data API is encapsulated to obtain real-time weather or future weather forecast data for a specified area.
    
    Parameters
    -------------------------------
    - area_code (int): indicates the region code. If provided, the region code is used to obtain weather data
    - address (str): indicates the address information. If the region code is provided but not provided, the region code is obtained based on the address
    - city (str): city name, used to assist in obtaining the area code based on the address
    forecasts (bool): Specifies whether to obtain real-time weather data (False) or future weather forecast data (True)
    
    Returns
    -------------------------------
    - dict: A dictionary containing weather information for the requested area.
    """

    check_param_type(area_code, int, "area_code"); 
    check_param_type(address, str, "address")
    check_param_type(city, str, "city")
    check_param_type(forecasts, bool, "forecasts")

    request_result: dict = {}
    with open("./pyprecip/_constant.json", "r", encoding="utf-8") as file:
        READ_API_DATA: dict = json.load(file)["READ_API"]    

    # 自动获取当前位置、根据地名获取区域编码 
    if area_code == -1 and address == "":
        # 自动获取当前的位置 
        URL: str = READ_API_DATA["LOCATION_URL"]
        PARAMS: dict = { "key": WEATHER_KEY }

        # 发送 request 请求 
        response = send_request(URL, PARAMS)            
        location_data: dict = response.json()

        if location_data["status"] == '1' and location_data["infocode"] == "10000":
            area_code = location_data["adcode"]
            request_result["area_code"] = location_data["adcode"]
        else:
            exc.raise_exception("An unknown error occurred with the ip location request. Please try again later", RequestException)
    elif area_code == -1 and address != "": 
        address_info = get_address_info(address=address, city=city)
        area_code = address_info["geocodes"][0]["adcode"]
        request_result["area_code"] = area_code
    else:
        if address != "": 
            warn.raise_warning("The area_code parameter overrides the effect of the address parameter.")
        request_result["area_code"] = area_code

    # 请求实时/未来的气候数据 
    WEATHER_URL = READ_API_DATA["WEATHER_URL"]
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
            for key_ in ["province", "city", "reporttime", "adcode"]:
                del forecasts_or_lives_copy[key_]
            forecasts_or_lives["casts"] = [forecasts_or_lives_copy]

        request_result["province"] = forecasts_or_lives["province"]
        request_result["city"] = forecasts_or_lives["city"]
        request_result["update_time"] = forecasts_or_lives["reporttime"] 
        request_result["casts"] = forecasts_or_lives["casts"]
        
        return request_result                    
    else:
        exc.raise_exception("An unknown error occurred in the climate data request. Please try again later", RequestException)



# test 
if __name__ == "__main__":
    result = get_weather_data(address="和平区")
    print(result)



