import json 
from ..utits.sundries import check_param_type
from ..utits.except_ import RaiseException as exc

def __check_param(func):
    def wrapper(*args, **kwargs):     
        if not args and not kwargs:
            exc.raise_exception("The raw_data parameter is required.",ValueError )
        return func(*args, **kwargs)
    return wrapper


@__check_param
def filter_invalid_data(raw_data: dict = {}) -> dict:
    """
    Filter invalid data and return a valid data dictionary.

    Parameters:
     - raw_data (dict): Raw data dictionary, where each key corresponds to a list, the first element of the list is the initial valid data list, and subsequent elements may be invalid data.

    Returns:
     - dict: Dictionary containing valid data, where each key corresponds to a list of the elements in the list that are valid data.
    """

    check_param_type(raw_data, dict, "raw_data"); 
    valid_data: dict = {} 

    for item in raw_data:
        valid_data[item] = [raw_data[item][0]]               
        ITEM_ELE_ = len(raw_data[item][0])  

        for seq_ele in raw_data[item][1:]:
            if isinstance(seq_ele, list) and (len(seq_ele) == ITEM_ELE_):
                if seq_ele not in valid_data[item]:
                    valid_data[item].append(seq_ele)

    return valid_data; 


@__check_param
def replace_invalid_data(raw_data: dict = {}, replace_value: (str|int) = 0)  -> dict:
    """
    Replaces invalid data in the original data and returns a valid data dictionary.

    Parameters:
     - raw_data (dict): Raw data dictionary, where each key corresponds to a list, the first element of the list is the initial valid data list, and subsequent elements may contain invalid data.
     - replace_value (str|int): A value used to replace invalid data. The default is 0.

    Returns:
     - dict: Dictionary containing valid data, where each key corresponds to a list of elements in which the valid data has been replaced with the specified replacement value.
    """

    check_param_type(raw_data, dict, "raw_data"); 
    valid_data: dict = {} 

    for item in raw_data:
        valid_data[item] = [raw_data[item][0]]               
        for seq_ele in raw_data[item][1:]:
            # 循环替换 
            for _ in range(len(seq_ele)):
                if None in seq_ele or "" in seq_ele:
                    idx = seq_ele.index(None) if None in seq_ele else seq_ele.index(""); 
                    seq_ele[idx] = replace_value
                else:
                    break; 
            valid_data[item].append(seq_ele)
        return valid_data; 


@__check_param
def remove_duplicate_data(raw_data: dict = {}) -> dict:
    """
    """     

    check_param_type(raw_data, dict, "raw_data");
    unique_data: dict = {}; 
        
    for item in raw_data:
        unique_data[item] = [raw_data[item][0]] 
        raw_data[item] = raw_data[item][1:]; 
        # 去重算法 - 待优化
        for sub_list in raw_data[item]:
            if sub_list not in unique_data[item]:
                unique_data[item].append(sub_list)

    return unique_data; 
    





# test 
if __name__ == "__main__":
    MULTI_DICT: dict = {}; 
    with open("./pyprecip/_constant.json", "r", encoding="utf-8") as file:
        MULTI_DICT: dict = json.load(file)["HANDLE_MISSING"]["TEST_MULTI_DICT"]  

    print(MULTI_DICT["weather_data"])
    print(len(MULTI_DICT["weather_data"])) 
    MULTI_DICT = remove_duplicate_data(MULTI_DICT)

    print(MULTI_DICT["weather_data"])
    print(len(MULTI_DICT["weather_data"])) 







