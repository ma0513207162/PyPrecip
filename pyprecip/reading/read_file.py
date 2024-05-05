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
def read_excel(path: str, row_read: bool = True, sheet_names: tuple = (), 
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
            temp_list = [] 
            for row in sheet_iter_rows:
                temp_list.append(list(row))
        else:
            """
            # 使用 map 和 lambda 函数列表生成式 
            lambda_func = lambda row: [row[idx-1] for idx in column_indices]
            temp_list = list(map(lambda_func, sheet_iter_rows))
            """
            # 保留指定的列序列 column_indices
            temp_list = [] 
            for row in sheet_iter_rows:
                _list = []
                for idx in column_indices:
                    if idx > 0 and idx <= len(row):
                        _list.append(row[idx-1])
                    else:
                        exc.raise_exception("The index must be greater than 0 and less than the sequence length.",IndexError )
                temp_list.append(_list)



        read_excel_result[sheet.title] = temp_list; 


    return read_excel_result



@__file_exists    
def read_csv(path: str, row_indices: (tuple|list) = (), column_indices: (tuple|list) = ()): 
    check_param_type(path, str, "path")
    check_param_type(row_indices, (tuple|list), "row_indices")
    check_param_type(column_indices, (tuple|list), "column_indices")

    """ 以列的方式进行读取 """
    read_csv_result: dict = {}

    with open(path, "r", encoding="gbk") as csv_file:
        reader_csv = list(csv.reader(csv_file)) 

    # 指定行范围  
    if isinstance(row_indices, list) and row_indices != []:
        row_indices.extend([1] * (3 - len(row_indices))) 
        start, end, _ = row_indices[0], row_indices[1], row_indices[2]
        reader_csv = reader_csv[start-1: end]
    # 指定行索引 
    if isinstance(row_indices, tuple) and row_indices != ():
        row_idx_list = []
        for idx in row_indices:
            if idx >= 1 and idx <= len(reader_csv):
                row_idx_list.append(reader_csv[idx-1]) 
            else:
                exc.raise_exception("The index must be greater than 0 and less than the sequence length.", IndexError)
        reader_csv = row_idx_list; 

    # ——————————————————
    reader_csv = list(zip(*reader_csv)) 
    # list 类型指定行范围  
    if isinstance(column_indices, list) and column_indices != []:
        column_indices.extend([1] * (3 - len(column_indices))) 
        start, end, _ = column_indices[0], column_indices[1], column_indices[2]; 
        reader_csv = reader_csv[start-1: end]
    # tuple 类型指定列索引 
    if isinstance(column_indices, tuple) and column_indices != ():
        col_idx_list = [] 
        for idx in column_indices:
            if idx >= 1 and idx <= len(reader_csv):
                col_idx_list.append(reader_csv[idx-1]); 
            else:
                exc.raise_exception("The index must be greater than 0 and less than the sequence length.", IndexError)
        reader_csv = col_idx_list;

    # 封装 dict 对象
    file_name = os.path.splitext(os.path.basename(path))[0]
    read_csv_result[file_name] = reader_csv; 

    return read_csv_result;  



# 以主进程的方式运行 
if __name__ == "__main__": 
    path = "./static/test_data.csv"
    reader_csv = read_csv(path=path, row_indices=[1,2], column_indices=[2,4]);

    for item in reader_csv["test_data"]:
        print(item)
    