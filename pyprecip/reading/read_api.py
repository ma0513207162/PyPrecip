import json
from requests.exceptions import RequestException 
from ..utits.http import send_request 
from ..utits.except_ import RaiseException as exc 
from ..utits.warn_ import RaiseWarn as warn


def get_address_info(address: str = "", city: str = None):
    if address != "":
        with open("./pyprecip/static/constant.json", "r", encoding="utf-8") as file:
            READ_API_DATA: dict = json.load(file)["READ_API"]    

        GEOCODING_URL: str = READ_API_DATA["GEOCODING_URL"]
        PARAMS: dict = { 
            "key": READ_API_DATA["WEATHER_KEY"], 
            "address": address,  "city": city
        }

        # 发送 request 请求 
        response = send_request(GEOCODING_URL, PARAMS)   
        address_info: dict = response.json()

        if address_info["status"] == "1" and address_info["infocode"] == "10000":
            if int(address_info["count"]) > 1:
                warn.raise_warning(f"The place name has multiple regional codes: {address}, the first one is selected by default.")

            geocodes_adcode = address_info["geocodes"][0]["adcode"]
            return geocodes_adcode
        else:
            except_address_info: str = address_info["info"]; 
            exc.raise_exception(f"An unknown error occurred in the address request. {except_address_info} \
                             Please try again later", RequestException)
    else:
        exc.raise_exception("address parameter cannot be null or invalid.", ValueError) 


def get_weather_data(area_code: int = -1, address: str = "", 
                     city: str = "", forecasts: bool = False) -> dict:
    if not isinstance(area_code, int):
        exc.raise_exception("area_code parameter must be of type int.", TypeError)
    if not isinstance(address, str):
        exc.raise_exception("address parameter must be of type str.", TypeError)
    if not isinstance(city, str):
        exc.raise_exception("city parameter must be of type str.", TypeError) 
    if not isinstance(forecasts, bool): 
        exc.raise_exception("forecasts parameter must be of type bool.", TypeError)

    request_result: dict = {}
    with open("./pyprecip/static/constant.json", "r", encoding="utf-8") as file:
        READ_API_DATA: dict = json.load(file)["READ_API"]    

    # 自动获取当前位置、根据地名获取区域编码 
    if area_code == -1 and address == "":
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
            exc.raise_exception("An unknown error occurred with the ip location request. Please try again later", RequestException)
    elif area_code == -1 and address != "": 
        area_code = get_address_info(address=address, city=city)
        request_result["area_code"] = area_code
    else:
        if address != "": 
            warn.raise_warning("The area_code parameter overrides the effect of the address parameter.")
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
        exc.raise_exception("An unknown error occurred in the climate data request. Please try again later", RequestException)



if __name__ == "__main__":
    result = get_weather_data(address="青山区2") 
    
    print(result)
