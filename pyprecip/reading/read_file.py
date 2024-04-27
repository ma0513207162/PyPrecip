from openpyxl import load_workbook
from csv import reader

def file_exists(func):
    def wrapper(*args, **kwargs):        
        if not args and not kwargs:
            raise TypeError("The file path is required.")  
        return func(*args, **kwargs)
    return wrapper


@file_exists
def read_csv(path: str, row: tuple = (), column: tuple = ()):
    reader_dict = {}; 
    
    with open(path, "r") as csv_file:
        reader_dict = list(reader(csv_file))      
        
    return reader_dict 


@file_exists
def read_excel(path: str, sheet_names: tuple = (), 
      rows_range: tuple = (), columns_range: tuple = (), 
      row_indices: tuple = (), column_indices: tuple = ()) -> dict:
    """
    - sheet_names: 工作表序列
    - rows_range: 行范围、 - columns_range: 列范围 
    - row_indices: 指定行的索引序列、 - column_indices: 指定列的索引序列 
    """
    workbook = load_workbook(filename = path, data_only = True)

    # 获取指定的工作表
    sheet_list = []
    if sheet_names != ():
        for sheet_name in sheet_names:
            sheet_list.append(workbook[sheet_name])
    else:
        sheet_list.append(workbook.active)
    
    # 读取指定的范围，用元组进行指定 
    if rows_range == (): rows_range = (1, 0); 
    if columns_range == (): columns_range = (1, 0);  

    reader_dict: dict = {} 
    for sheet in sheet_list:
        # rows_range columns_range 
        sheet_iter_rows  = sheet.iter_rows(min_row = rows_range[0], max_row = rows_range[1],
            min_col = columns_range[0], max_col = columns_range[1], values_only = True) 
        sheet_iter_rows: list = list(sheet_iter_rows)           

        # row_indices column_indices
        if row_indices != (): 
            temp_iter_rows = []
            for idx in row_indices:
                if idx > 0 and len(sheet_iter_rows) > idx:
                    temp_iter_rows.append(sheet_iter_rows[idx-1]) 
            sheet_iter_rows = temp_iter_rows


        if column_indices == ():
            temp_row_list = [] 
            for row in sheet_iter_rows:
                temp_row_list.append(list(row))
            reader_dict[sheet.title] = temp_row_list;
        else:
            temp_col_list = [] 
            for row in sheet_iter_rows:
                temp_list = []
                for idx in column_indices:
                    temp_list.append(row[idx-1]) 
                temp_col_list.append(temp_list)
            reader_dict[sheet.title] = temp_col_list
    return reader_dict


    
# 以主进程的方式运行 
if __name__ == "__main__": 
    path = "./static/files/weather_data.xlsx"
    reader_dict = read_excel(path, sheet_names= ("Sheet1", "Sheet2"), 
                            rows_range=(1, 10), columns_range=(1,5), 
                            row_indices= (1), column_indices=(1))    

    for item in reader_dict:
        for value in reader_dict[item]:
            print(value)
        print("=" * 60)
    
   
    


    



    


