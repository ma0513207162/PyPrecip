import json 
from ..utits.sundries import check_param_type
from ..utits.except_ import RaiseException as exc

# def clean_data(): pass 

def __check_param(func):
    def wrapper(*args, **kwargs):     
        if not args and not kwargs:
            exc.raise_exception("The raw_data parameter is required.",ValueError )
        return func(*args, **kwargs)
    return wrapper


@__check_param
def handle_multi_dict(raw_data: dict = {}, replace: bool = False, 
                      replace_value: (str|int) = 0) -> dict:
    """
    数据清洗：过滤掉数据中的错误值、缺失值、重复值、异常值等，以确保数据质量和准确性。
    缺失值处理：处理数据中的缺失值，可以通过删除缺失值、插值填充、使用默认值等方法来处理。
    参数不允许为空 
    """
    """
    递归过滤多维列表中的缺失数据(None和空字符串)
    
    Args:
        data (list): 待处理的多维列表数据
        
    Returns:
        list: 过滤后的列表
    """

    check_param_type(raw_data, dict, "raw_data"); 
    multi_dict = {}; 

    if replace:       
        print(replace_value) 
        for item in raw_data["weather_data"]:
            print(item)
    else:
        for item in raw_data:
            multi_dict[item] = []           # 初始化一个 item 对象 
            ITEM_ELE_ = len(raw_data[item][0]); 

            for list_ele in raw_data[item]:
                # 过滤错误值、缺失值、重复值、异常值
                # 必须是 list 类型、不能为空列表、长度与行头一致 
                if not list_ele and len(list_ele) == ITEM_ELE_:
                    if list_ele not in multi_dict[item]:
                        multi_dict[item].append(list_ele)
                    

    return multi_dict; 

# test 
if __name__ == "__main__":
    MULTI_DICT: dict = {}; 
    with open("./pyprecip/_constant.json", "r", encoding="utf-8") as file:
        MULTI_DICT: dict = json.load(file)["HANDLE_MISSING"]["TEST_MULTI_DICT"]  

    handle_result = handle_multi_dict(MULTI_DICT); 
    print(handle_result)






