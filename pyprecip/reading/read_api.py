import requests, json 


def get_weather_data(area_code: int = -1, forecasts: bool = False) -> dict:
    if type(area_code) != int:
        raise TypeError("The area_code parameter type must be int.") 
    elif type(forecasts) != bool:
        raise TypeError("The type of forecasts parameter must be bool.") 
        
    request_result: dict = {}
    with open("./static/constant.json", "r") as file:
        READ_API_DATA = json.load(file)["READ_API"]    

    if area_code == -1:
        URL: str = READ_API_DATA["LOCATION_URL"]
        PARAMS: dict = { "key": READ_API_DATA["LOCATION_KEY"] }
        response = requests.get(URL, params = PARAMS)
        location_data: dict = response.json()
        
        if location_data["status"] == '1' and location_data["infocode"] == "10000":
            area_code = location_data["adcode"]
            request_result["area_code"] = location_data["adcode"]
        else:
            raise Exception("An unknown error occurred with the ip location request. Please try again later")
    else:
        request_result["area_code"] = area_code

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
            forecasts_or_lives["casts"] = [forecasts_or_lives_copy]

        request_result["province"] = forecasts_or_lives["province"]
        request_result["city"] = forecasts_or_lives["city"]
        request_result["update_time"] = forecasts_or_lives["reporttime"] 
        request_result["casts"] = forecasts_or_lives["casts"]
        
        return request_result                    
    else:
        raise Exception("An unknown error occurred in the climate data request. Please try again later")
    

if __name__ == "__main__":
    get_weather_data()


