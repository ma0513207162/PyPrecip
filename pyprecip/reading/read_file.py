from openpyxl import load_workbook
import os, csv 


class ReadFile:
    def __init__(self, row_range: tuple = (), column_range: tuple = (), 
                row_indices: tuple = (), column_indices: tuple = ()) -> None:
        """
        Initializes the class instance with file path and optional ranges/indices.

        Args:
            file_path (str): The path to the file to be read.
            row_range (tuple, optional): A tuple specifying the row range (start, end) to read. Defaults to ().
            column_range (tuple, optional): A tuple specifying the column range (start, end) to read. Defaults to ().
            row_indices (tuple, optional): A tuple of row indices to read. Defaults to ().
            column_indices (tuple, optional): A tuple of column indices to read. Defaults to ().

        Raises:
            FileNotFoundError: If the specified file path does not exist.
            TypeError: If any of the range or indices arguments are not of the correct type.
        """

        # # Check for file existence
        # if not os.path.exists(file_path):
        #     raise FileNotFoundError(f"File not found: {file_path}")

        # Validate ranges/indices types
        if not isinstance(row_range, tuple):
            raise TypeError("row_range must be a tuple of two integers (start, end).")
        if not isinstance(column_range, tuple):
            raise TypeError("column_range must be a tuple of two integers (start, end).")
        if not isinstance(row_indices, tuple):
            raise TypeError("row_indices must be a tuple of integers.")
        if not isinstance(column_indices, tuple):
            raise TypeError("column_indices must be a tuple of integers.")

        # Initializes instance parameters
        self._row_range = row_range
        self._column_range = column_range 
        self._row_indices = row_indices 
        self._column_indices = column_indices


    def read_betcdf(self):
        pass 
    
    def read_excel(self, file_path: str, sheet_names: tuple = ()) -> dict:
        workbook = load_workbook(filename = file_path, data_only = True)

        # Gets the specified worksheet 
        sheet_list = []
        if sheet_names != ():
            for sheet_name in sheet_names:
                sheet_list.append(workbook[sheet_name])
        else:
            sheet_list.append(workbook.active)

        # 元组指定读取的范围
        if self._row_range == (): self._row_range = (1, 0); 
        if self._column_range == (): self._column_range = (1, 0);  

        read_excel_result: dict = {} 
        for sheet in sheet_list:
            # 指定行和列范围 row_range column_range 
            sheet_iter_rows  = sheet.iter_rows(min_row = self._row_range[0], max_row = self._row_range[1],
                min_col = self._column_range[0], max_col = self._column_range[1], values_only = True) 
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
            
            # 封装二维序列返回
            if self._column_indices == ():
                temp_row_list = [] 
                for row in sheet_iter_rows:
                    temp_row_list.append(list(row))
                read_excel_result[sheet.title] = temp_row_list;
            else:
                # 保留指定的列序列 column_indices
                lambda_func = lambda row: [row[idx-1] for idx in self._column_indices]
                temp_col_list = list(map(lambda_func, sheet_iter_rows))
                read_excel_result[sheet.title] = temp_col_list
            
        return read_excel_result


    def read_csv(self, file_path: str): 
        read_csv_result: dict = {}

        with open(path, "r", encoding="gbk") as csv_file:
            reader_rows_list = list(csv.reader(csv_file)) 
        file_name = os.path.splitext(os.path.basename(file_path))[0]

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


def read_test():
    print("read test")

# 以主进程的方式运行 
if __name__ == "__main__": 
    path = "./static/files/weather_data.xlsx"
    read_file = ReadFile(path)

    read_excel_result = read_file.read_excel() 

    for item in read_excel_result:
        for i in read_excel_result[item]:
            print(i) 
    