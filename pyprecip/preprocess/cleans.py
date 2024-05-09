import json
from math import dist  
from typing import List 
from ..utits.sundries import check_param_type
from ..utits.except_ import RaiseException as exc

def __check_param(func):
    def wrapper(*args, **kwargs):     
        if not args and not kwargs:
            exc.raise_exception("The raw_data parameter is required.",ValueError )
        return func(*args, **kwargs)
    return wrapper

"""
@__check_param
def normalize_data(raw_data: List[(str|int)]):
    check_param_type(raw_data, list, "raw_data"); 
    normalize_result: List[list] = [];

    for data in raw_data:
        temp_list = []; 
        for item in data:
            if isinstance(item, (str, int, float, complex)):
                temp_list.append(str(item));
            elif isinstance(item, (tuple, list, set)):
                temp_list.extend(item)
            elif isinstance(item, bool):
                temp_list.append(1 if bool == True else False);             
            elif isinstance(item, dict):
                temp_list.extend(dict.values());  
                temp_list.extend(dict.keys());
            else:
                temp_list.append(item);
        normalize_result.append(temp_list); 
    return normalize_result; 
"""


@__check_param
def process_invalid_data(raw_data: List[(str|int)], remove_invalid: bool = False, 
    remove_rows: bool = False, replace_value: (str|int) = 0, invalid_value: tuple = (None, "")) -> list:
    """
    This function is used to process a list that contains invalid data.

    Parameters:
     - raw_data: List[(str|int)] - A list of raw data to be processed, which can contain strings or integers.
     - remove_invalid: bool - Indicates whether invalid data needs to be deleted. The default value is False.
     - remove_rows: bool - Indicates whether an entire row containing invalid data needs to be deleted. The default is False.
     - replace_value: (str|int) - A value used to replace invalid data. The default is 0.
     - invalid_value: tuple - Specifies a tuple of invalid data values. The default is (None, "").

    Returns:
     - List[(str|int)] - The list of valid processed data.
    """
    
    check_param_type(raw_data, list, "raw_data");  
    check_param_type(remove_invalid, bool, "remove_invalid");  
    check_param_type(invalid_value, tuple, "invalid_value");  
    check_param_type(remove_rows, bool, "remove_rows");  
    check_param_type(replace_value, (str|int), "replace_value");  
    valid_data: List[(str|int)] = [];           

    if remove_invalid:
        if remove_rows:
            # 删除整行 
            for data in raw_data:
                if not any(inv in data for inv in invalid_value):
                    valid_data.append(data)
        else:
            # 删除单元格 
            for data in raw_data:
                data = list(filter(lambda x: x not in invalid_value, data)); 
                valid_data.append(data);
    else:       
        # 替换值 
        for data in raw_data:
            for inv in invalid_value:
                MAX_LOOPS, loop_count = len(data), 0
                while (inv in data) and (replace_value not in invalid_value):
                    data[data.index(inv)] = replace_value;
                    loop_count += 1; 
                    if loop_count > MAX_LOOPS:
                        exc.raise_exception(f"Loop exceeded maximum iterations ({MAX_LOOPS})", RuntimeError); 
        valid_data = raw_data;

    return valid_data


@__check_param
def remove_duplicate_data(raw_data: List[(str|int)], approx_dele: bool = False) -> list:
    """
    (需要优化)
    Removes duplicate elements from a given list.

    Parameters
     - raw_data (List[(str|int)]): A list of raw data containing strings or integers.
     - approx_dele (bool, optional): Indicates whether to perform an approximate deduplication operation. The default is False.

    Returns
     - list: A new list with no duplicate elements. 
    """
    
    check_param_type(raw_data, list, "raw_data"); 
    check_param_type(approx_dele, bool, "approx_dele");
    unique_data = []; 

    if approx_dele:
        # 近似去重(数值类型)
        for data in raw_data:
            is_approx, data_len = False, len(data) 
            for exist in unique_data:
                if data_len == len(exist) and dist(data, exist) < 0.1: 
                    is_approx = True; break; 
            if not is_approx: 
                unique_data.append(data); 
    else: 
        # 简单去重 
        for data in raw_data:
            if data not in unique_data:
                unique_data.append(data)
    return unique_data;





# 以主进程的方式运行 
if __name__ == "__main__":
    with open("./static/test_data.json", "r", encoding="utf-8") as file:
        duplicate_data: dict = json.load(file)["row_data"]
   


 



    