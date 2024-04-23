import sys

sys.path.append("../pyprecip")
from pyprecip.reading.read_file import read_excel



if __name__ == "__main__": 
    result = read_excel("./static/test_data.xlsx"); 

    print(result)    





