from openpyxl import load_workbook
from typing import Tuple
import os, csv 


class ReadFile:
    def __init__(self, file_path: str, rows_range: Tuple[int, int] = (), columns_range: Tuple[int, int] = (), 
                row_indices: Tuple[int, int] = (), column_indices: Tuple[int, int] = ()) -> None:
        """
        Initializes the class instance with file path and optional ranges/indices.

        Args:
            file_path (str): The path to the file to be read.
            rows_range (Tuple[int, int], optional): A tuple specifying the row range (start, end) to read. Defaults to ().
            columns_range (Tuple[int, int], optional): A tuple specifying the column range (start, end) to read. Defaults to ().
            row_indices (Tuple[int], optional): A tuple of row indices to read. Defaults to ().
            column_indices (Tuple[int], optional): A tuple of column indices to read. Defaults to ().
        
        Raises:
            FileNotFoundError: If the specified file path does not exist.
            TypeError: If any of the range or indices arguments are not of the correct type.
        """

        # Check for file existence
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Validate ranges/indices types
        if not isinstance(rows_range, Tuple[int, int]):
            raise TypeError("rows_range must be a tuple of two integers (start, end).")
        if not isinstance(columns_range, Tuple[int, int]):
            raise TypeError("columns_range must be a tuple of two integers (start, end).")
        if not isinstance(row_indices, Tuple[int]):
            raise TypeError("row_indices must be a tuple of integers.")
        if not isinstance(column_indices, Tuple[int]):
            raise TypeError("column_indices must be a tuple of integers.")

        # Initializes instance parameters
        self._file_path = file_path
        self._row_range = rows_range
        self._column_range = columns_range 
        self._row_indices = row_indices 
        self._column_indices = column_indices

    def read_betcdf(self):
        pass 

    def read_csv(self): 
        read_csv_result: dict = {}

        with open(path, "r", encoding="gbk") as csv_file:
            reader_rows_list = list(csv.reader(csv_file)) 
        file_name = os.path.splitext(os.path.basename(self._file_path))[0]

        if self._row_range != ():
            reader_rows_list = reader_rows_list[self._row_range[0], self._row_range[1]]

        if self._column_range != ():
            temp_col_list = [] 
            for row in reader_rows_list:
                _list = []
                for idx in self._column_range:
                    _list.append(row[idx-1])
                temp_col_list.append(_list)
            reader_rows_list = temp_col_list

        read_csv_result[file_name] = reader_rows_list
        return read_csv_result;

    def read_excel(self, sheet_names: tuple = ()) -> dict:
        """
        - sheet_names: 工作表序列
        - rows_range: 行范围、 - columns_range: 列范围 
        - row_indices: 指定行的索引序列、 - column_indices: 指定列的索引序列 
        row_indices 和 column_indices 是在 rows_range 和 columns_range 两者的基础上进行处理的。 
        """
        workbook = load_workbook(filename = self._file_path, data_only = True)

        # 获取指定的工作表
        sheet_list = []
        if sheet_names != ():
            for sheet_name in sheet_names:
                sheet_list.append(workbook[sheet_name])
        else:
            sheet_list.append(workbook.active)
        
        # 元组指定读取的范围
        if rows_range == (): rows_range = (1, 0); 
        if columns_range == (): columns_range = (1, 0);  

        read_excel_result: dict = {} 
        for sheet in sheet_list:
            # 指定行和列范围 rows_range columns_range 
            sheet_iter_rows  = sheet.iter_rows(min_row = rows_range[0], max_row = rows_range[1],
                min_col = columns_range[0], max_col = columns_range[1], values_only = True) 
            sheet_iter_rows: list = list(sheet_iter_rows)           

            # 保留指定的行序列 row_indices
            if self._row_indices != (): 
                temp_iter_rows = []
                for idx in self._row_indices:
                    if idx > 0 and idx < len(sheet_iter_rows):
                        temp_iter_rows.append(sheet_iter_rows[idx-1]) 
                    else:
                        raise IndexError("The index must be greater than 0 and less than the sequence length.");
                sheet_iter_rows = temp_iter_rows
            
            # 
            if self._column_indices == ():
                temp_row_list = [] 
                for row in sheet_iter_rows:
                    temp_row_list.append(list(row))
                read_excel_result[sheet.title] = temp_row_list;
            else:
                # 保留指定的列序列 column_indices
                temp_col_list = [] 
                for row in sheet_iter_rows:
                    _list = []
                    for idx in self._column_indices: 
                        _list.append(row[idx-1]) 
                    temp_col_list.append(_list)
                read_excel_result[sheet.title] = temp_col_list
            
        return read_excel_result


     



# 以主进程的方式运行 
if __name__ == "__main__": 
    path = "./static/files/weather_data.xlsx"
    read_file = ReadFile()
    



    


