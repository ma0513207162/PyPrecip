from openpyxl import load_workbook
from typing import List 
import os, csv


def file_exists(func):
    def wrapper(*args, **kwargs):
        csv_path = args[0]
        if not os.path.exists(csv_path):
            raise FileExistsError(f"File '{csv_path}' does not exist")
        return func(*args, **kwargs)
    return wrapper


@file_exists
def read_excel(excel_path: str, sheet_name: str = "Sheet1") -> List[List[str]]:
    """
    How to read an excel file
    - excel_path (str): specifies the path to the excel file
    - sheet_name (str): indicates the name of an excel table, The default value is Sheet1
    list: Returns a two-dimensional list of read completions
    """
    
    reader_list:List[List[str]] = []

    workbook = load_workbook(filename = excel_path, data_only=True)
    sheet = workbook[sheet_name]

    for row in sheet.iter_rows(values_only=True):
        reader_list.append(list(row))

    return reader_list; 

                
@file_exists
def read_csv(csv_path: str) -> List[List[str]]:
    """
    How to read a csv file
    -csv_path (str): indicates the path of the csv file
    list: Returns a two-dimensional list of read completions
    """

    reader_list: List[List[str]] = []; 

    with open(csv_path, "r") as csv_file:
        reader = csv.reader(csv_file)          
        reader_list = list(reader)
        
    return reader_list
    

if __name__ == "__main__": 
    # csv_path = "./static/weather_data.csv"
    # reader_list = read_csv(csv_path);

    excel_path = "./static/test_data.xlsx"
    reader_list = read_excel(excel_path)
    print(reader_list)




    
    










    
   
    


    



    


