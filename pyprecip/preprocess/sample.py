import json, random 

def system():
    pass 


def simple_random(data: list, sample_size: int):
    """
    Sample the sample_size row randomly from the two-dimensional list data

    Parameters
    -------------------------------
     - data (list): raw 2D data
     - sample_size (int): Sample size to be extracted

    Returns
    -------------------------------
     - list: indicates the sample data
    """
    # 检查输入是否合法
    if not isinstance(data, list) or not data:
        raise ValueError("输入数据必须是非空列表")
    if not isinstance(sample_size, int) or sample_size <= 0:
        raise ValueError("样本量必须是正整数")
    if sample_size > len(data):
        raise ValueError("样本量不能超过原始数据行数")
    
    # 构建索引列表
    indices = list(range(len(data)))
    
    # 随机打乱索引
    random.shuffle(indices)
    
    # 根据样本量获取对应索引的数据行
    sample_indices = indices[:sample_size]
    sample = [data[i] for i in sample_indices]
    
    return sample  



if __name__ == "__main__":
    MULTI_DICT: dict = {}; 
    with open("./pyprecip/_constant.json", "r", encoding="utf-8") as file:
        MULTI_DICT: dict = json.load(file)["HANDLE_MISSING"]["TEST_MULTI_DICT"]  

    print(MULTI_DICT["weather_data"])
    # print(len(MULTI_DICT["weather_data"])) 


