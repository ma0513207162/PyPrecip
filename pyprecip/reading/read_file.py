import os, csv
from openpyxl import load_workbook
from ..utits.except_ import RaiseException as exc 
from ..utits.sundries import check_param_type


def __file_exists(func):
    def wrapper(*args, **kwargs):     
        if not args and not kwargs:
            exc.raise_exception("The file path is required.", TypeError) 
        return func(*args, **kwargs)
    return wrapper 


@__file_exists    
def read_excel(path: str, sheet_names: tuple = (), 
               row_range: tuple = (), column_range: tuple = (), 
            row_indices: tuple = (), column_indices: tuple = ()) -> dict:
    workbook = load_workbook(filename = path, data_only = True)

    # Gets the specified worksheet 
    sheet_list = []
    if sheet_names != ():
        for sheet_name in sheet_names:
            sheet_list.append(workbook[sheet_name])
    else:
        sheet_list.append(workbook.active)

    # 元组指定读取的范围
    if row_range == (): row_range = (1, 0); 
    if column_range == (): column_range = (1, 0);  

    read_excel_result: dict = {} 
    for sheet in sheet_list:
        # 指定行和列范围 row_range column_range 
        sheet_iter_rows  = sheet.iter_rows(min_row = row_range[0], max_row = row_range[1],
            min_col = column_range[0], max_col = column_range[1], values_only = True) 
        sheet_iter_rows: list = list(sheet_iter_rows)           

        # 保留指定的行序列 row_indices
        if row_indices != ():
            temp_iter_rows = []
            for idx in row_indices:
                if idx > 0 and idx <= len(sheet_iter_rows):
                    temp_iter_rows.append(sheet_iter_rows[idx-1]) 
                else:
                    exc.raise_exception("The index must be greater than 0 and less than the sequence length.", IndexError)
            sheet_iter_rows = temp_iter_rows
                                        
        # 封装二维序列返回
        if column_indices == ():
            temp_row_list = [] 
            for row in sheet_iter_rows:
                temp_row_list.append(list(row))
            read_excel_result[sheet.title] = temp_row_list;
        else:
            """
            # 使用 map 和 lambda 函数列表生成式 
            lambda_func = lambda row: [row[idx-1] for idx in column_indices]
            temp_col_list = list(map(lambda_func, sheet_iter_rows))
            """
            # 保留指定的列序列 column_indices
            temp_col_list = [] 
            for row in sheet_iter_rows:
                _list = []
                for idx in column_indices:
                    if idx > 0 and idx <= len(row):
                        _list.append(row[idx-1])
                    else:
                        exc.raise_exception("The index must be greater than 0 and less than the sequence length.",IndexError )
                temp_col_list.append(_list)
            read_excel_result[sheet.title] = temp_col_list


    return read_excel_result


@__file_exists    
def read_csv(path: str, column_read: bool = True, row_range: tuple = (), column_range: tuple = (), 
            row_indices: tuple = (), column_indices: tuple = ()): 
    read_csv_result: dict = {}

    with open(path, "r", encoding="gbk") as csv_file:
        reader_rows_list = list(csv.reader(csv_file)) 

    # 指定行和列范围 row_range column_range 
    if row_range != ():
        start, end = row_range
        reader_rows_list = reader_rows_list[start-1: end]
       
    if column_range != ():
        temp_row_list = []
        for row in reader_rows_list:
            row_ = row[column_range[0]-1: column_range[1]]
            temp_row_list.append(row_) 
        reader_rows_list = temp_row_list

    # 保留指定的行序列 row_indices
    if row_indices != ():
        row_idx_list = []
        for idx in row_indices:
            if idx >= 1 and idx <= len(reader_rows_list):
                row_idx_list.append(reader_rows_list[idx-1]) 
            else:
                exc.raise_exception("The index must be greater than 0 and less than the sequence length.", IndexError)
        reader_rows_list = row_idx_list 
    
    # 保留指定的列序列 column_indices
    if column_indices != ():
        temp_col_list = [] 
        for row in reader_rows_list:
            _list = []
            for idx in column_indices:
                if idx > 0 and idx <= len(row):
                    _list.append(row[idx-1])
                else:
                    exc.raise_exception("The index must be greater than 0 and less than the sequence length.", IndexError)
            temp_col_list.append(_list)
        reader_rows_list = temp_col_list

    # 按列读取 
    if column_read:
        reader_rows_list = [list(pair) for pair in zip(*reader_rows_list)] 

    file_name = os.path.splitext(os.path.basename(path))[0]
    read_csv_result[file_name] = reader_rows_list
    return read_csv_result  



# 以主进程的方式运行 
if __name__ == "__main__": 
    path = "./static/weather_data.csv"
    read_result = read_csv(path=path, column_read=True, row_range=(1,5));
    print(read_result)