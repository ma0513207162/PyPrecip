import os, csv

def read_excel(excel_path: str):
    """
    workbook = xlrd.open_workbook('test.xlsx')
    sheet = workbook.sheet_by_name('Sheet1')
    value = sheet.cell_value(1, 1)

    # 打印值
    print(value)
    """
    pass 


def read_csv(csv_path: str) -> list:
    if not os.path.exists(csv_path):  
        raise FileExistsError

    reader_list: list = []
    with open(csv_path, "r") as csv_file:
        reader = csv.reader(csv_file)           # reader object 
        reader_list = list(reader)
        
    return reader_list










    
   
    


    



    


