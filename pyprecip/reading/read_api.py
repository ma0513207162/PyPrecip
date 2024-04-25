import requests, json 

# def validate_parameter_format():
#     def wrapper(*args, **kwargs):        
#         if not args:
#             raise TypeError("path argument is required"); 
#     return wrapper


def get_weather_data(area_code: int = -1, forecasts: bool = False) -> dict:
    request_result = {}
    with open("./static/constant.json", "r") as file:
        READ_API_DATA = json.load(file)["READ_API"]    

    if area_code == -1:
        URL = READ_API_DATA["LOCATION_URL"]
        PARAMS = { "key": READ_API_DATA["LOCATION_KEY"] }
        response = requests.get(URL, params = PARAMS)
        location_data = response.json()
        
        if location_data["status"] == '1' and location_data["infocode"] == "10000":
            area_code = location_data["adcode"]
            request_result["area_code"] = location_data["adcode"]
        else:
            raise Exception("An unknown error occurred with the ip location request. Please try again later")
    else:
        request_result["area_code"] = location_data["adcode"] 

    # 请求实时/未来的气候数据 
    WEATHER_URL = READ_API_DATA["WEATHER_URL"]
    WEATHER_KEY = READ_API_DATA["WEATHER_KEY"]
    ext_type = "base" if forecasts == False else "all" 
    PARAMS = {"city": area_code,  "key": WEATHER_KEY, "extensions": ext_type}

    response = requests.get(WEATHER_URL, params = PARAMS); 
    weather_data = response.json()

    if weather_data["status"] == '1' and weather_data["infocode"] == '10000':
        if forecasts: 
            forecasts_or_lives = weather_data["forecasts"][0]
        else:
            forecasts_or_lives = weather_data["lives"][0]
            forecasts_or_lives_copy = forecasts_or_lives.copy()
            for key in ["province", "city", "reporttime", "adcode"]:
                del forecasts_or_lives_copy[key]
            forecasts_or_lives["casts"] = forecasts_or_lives_copy

        request_result["province"] = forecasts_or_lives["province"]
        request_result["city"] = forecasts_or_lives["city"]
        request_result["update_time"] = forecasts_or_lives["reporttime"] 
        request_result["casts"] = forecasts_or_lives["casts"]

        return request_result                    
    else:
        raise Exception("An unknown error occurred in the climate data request. Please try again later")
    


if __name__ == "__main__":
    result = get_weather_data(forecasts = True)
    print(result["casts"])


