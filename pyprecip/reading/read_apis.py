import requests

def validate_parameter_format():
    def wrapper(*args, **kwargs):        
        if not args:
            raise TypeError("path argument is required"); 
            
    return wrapper


def get_weather_data(area_code: int = 440513, area_name: str = "", type: int = 1) -> dict:
    
    
    GAO_DE_API = "d81aece9933c31b8c15920517061581b";
    GAO_DE_URL = "https://restapi.amap.com/v3/weather/weatherInfo"
    type = "base" if type == 1 else "all"; 

    PARAMS = { 
        "city": area_code,  "key": GAO_DE_API, 
        "extensions": "all", "output": "JSON"
    }
        
    response = requests.get(GAO_DE_URL, params = PARAMS); 
    weather_data = response.json()
    
    # if weather_data["status"] == 1 and weather_data["infocode"] == '10000':
    #     lives = weather_data["lives"][0]
    #     return lives
    # else:
    #     raise Exception("An unknown error occurred. Please try again later")

if __name__ == "__main__":
    get_weather_data(440513); 

