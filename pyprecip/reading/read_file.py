from openpyxl import load_workbook
from typing import List 
import os, csv


def file_exists(func):
    def wrapper(*args, **kwargs):        
        if not args:
            raise TypeError("path argument is required"); 
        
        file_path = args[0]
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' does not exist")
        return func(*args, **kwargs)
    return wrapper



@file_exists
def read_excel(path: str, sheet_name: str = "Sheet1") -> List[List[str]]:
    """
    How to read an excel file
    - path (str): specifies the path to the excel file
    - sheet_name (str): indicates the name of an excel table, The default value is Sheet1
    list: Returns a two-dimensional list of read completions
    """
    
    reader_list:List[List[str]] = []

    workbook = load_workbook(filename = path, data_only=True)
    sheet = workbook[sheet_name]

    for row in sheet.iter_rows(values_only=True):
        reader_list.append(list(row))

    return reader_list; 

                
@file_exists
def read_csv(path: str) -> List[List[str]]:
    """
    How to read a csv file
    -path (str): indicates the path of the csv file
    list: Returns a two-dimensional list of read completions
    """
    reader_list: List[List[str]] = []; 

    with open(path, "r") as csv_file:
        reader_list = list(csv.reader(csv_file))      
        
    return reader_list
    

if __name__ == "__main__": 
    # path = "./static/weather_data.csv"
    # reader_list = read_csv(path);
    path = "./static/test_data.xlsx"
    reader_list = read_excel(path)
    # print(reader_list)




    
    










    
   
    


    



    


