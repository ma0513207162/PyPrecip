import requests, json 

def validate_parameter_format():
    def wrapper(*args, **kwargs):        
        if not args:
            raise TypeError("path argument is required"); 
            
    return wrapper


def get_weather_data(area_code: int = 100000, forecasts: bool = False) -> dict:
    GAO_DE_API = "d81aece9933c31b8c15920517061581b"
    GAO_DE_URL = "https://restapi.amap.com/v3/weather/weatherInfo" 
    ext_type = "base" if forecasts == False else "all" 

    PARAMS = { 
        "city": area_code,  "key": GAO_DE_API, 
        "extensions": ext_type , "output": "JSON"
    }
    response = requests.get(GAO_DE_URL, params = PARAMS); 
    weather_data = response.json()

  
    if weather_data["status"] == '1' and weather_data["infocode"] == '10000':
        if forecasts: 
            """
            {'city': '潮阳区', 'adcode': '440513', 'province': '广东', 'reporttime': '2024-04-25 00:00:27',
                'casts': [
                    {'date': '2024-04-25', 'week': '4', 'dayweather': '中雨', 'nightweather': '大雨', 'daytemp': '25', 'nighttemp': '21', 'daywind': '北', 'nightwind': '北', 'daypower': '1-3', 'nightpower': '1-3', 'daytemp_float': '25.0', 'nighttemp_float': '21.0'},
                    {'date': '2024-04-26', 'week': '5', 'dayweather': '暴雨', 'nightweather': '阵雨', 'daytemp': '25', 'nighttemp': '22', 'daywind': '北', 'nightwind': '北', 'daypower': '1-3', 'nightpower': '1-3', 'daytemp_float': '25.0', 'nighttemp_float': '22.0'}, 
                    {'date': '2024-04-27', 'week': '6', 'dayweather': '阵雨', 'nightweather': '中雨', 'daytemp': '27', 'nighttemp': '22', 'daywind': '北', 'nightwind': '北', 'daypower': '1-3', 'nightpower': '1-3', 'daytemp_float': '27.0', 'nighttemp_float': '22.0'}, 
                    {'date': '2024-04-28', 'week': '7', 'dayweather': '大雨', 'nightweather': '阵雨', 'daytemp': '27', 'nighttemp': '22', 'daywind': '北', 'nightwind': '北', 'daypower': '1-3', 'nightpower': '1-3', 'daytemp_float': '27.0', 'nighttemp_float': '22.0'}
                ]
            }
            """
            forecasts = weather_data["forecasts"][0]
            # city, province, reporttime = forecasts['city'], forecasts['province'],  forecasts['reporttime']
            # casts = forecasts['casts']
            return forecasts
        else:
            """
            {'province': '广东', 'city': '潮阳区', 'adcode': '440513', 
            'weather': '多云', 'temperature': '21', 'winddirection': '东', 
            'windpower': '≤3', 'humidity': '81', 'reporttime': '2024-04-25 00:00:27', 
            'temperature_float': '21.0', 'humidity_float': '81.0'}
            """
            lives = weather_data["lives"][0]
            # city, province, reporttime = lives['city'], lives['province'],  lives['reporttime']
            return lives
    else:
        raise Exception("An unknown error occurred. Please try again later")
    


if __name__ == "__main__":
    result = get_weather_data(area_code = 100000, forecasts = True)
    print(result)

    

