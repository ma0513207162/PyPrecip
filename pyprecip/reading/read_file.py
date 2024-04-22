from openpyxl import load_workbook
import os, csv


def file_exists(func):
    def wrapper(*args, **kwargs):
        csv_path = args[0]
        if not os.path.exists(csv_path):
            raise FileExistsError(f"File '{csv_path}' does not exist")
        return func(*args, **kwargs)
    return wrapper



@file_exists
def read_excel(excel_path: str, sheet_name: str = "Sheet1") -> list:
    reader_list:list = []

    workbook = load_workbook(filename = excel_path)
    sheet = workbook[sheet_name]

    for row in sheet.iter_rows(min_row=1, max_row=1, min_col=1, max_col=1):
        for cell in row:
            print(cell.value)




@file_exists
def read_csv(csv_path: str) -> list:
    reader_list: list = []

    with open(csv_path, "r") as csv_file:
        reader = csv.reader(csv_file)          
        reader_list = list(reader)
        
    return reader_list
    

if __name__ == "__main__": 
    csv_path = "./static/weather_data.csv"
    reader_list = read_csv(csv_path); 


    
    










    
   
    


    



    


