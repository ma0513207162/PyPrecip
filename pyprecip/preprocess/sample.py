import json, random;  
from ..utits.sundries import check_param_type
from ..utits.except_ import RaiseException as exc
  

# 简单随机选择 
def simple_random_sample(raw_data: list, sample_size: int, seed: int = None):
    """
    """
    check_param_type(raw_data, list, "raw_data");
    check_param_type(sample_size, int, "sample_size");
    check_param_type(seed, (int|None), "seed");

    if sample_size <= 0:
        exc.raise_exception("The sample size must be greater than 0", ValueError)
    if sample_size > len(raw_data):
        exc.raise_exception("The sample size cannot be larger than the original data length", ValueError)

    # 随机种子  
    if seed is not None: 
        random.seed(seed); 
    
    indices = list(range(len(raw_data)));
    random.shuffle(indices);   
    
    # 根据样本量获取对应索引的数据行
    sample_indices = indices[:sample_size]
    sample_result = [raw_data[i] for i in sample_indices]
    
    return sample_result; 

# 系统抽样 
def system_sample(raw_data: list, sample_size: int):
    """
    """
    check_param_type(raw_data, list, "raw_data");
    check_param_type(sample_size, int, "sample_size");

    if sample_size <= 0:
        exc.raise_exception("The sample size must be greater than 0", ValueError)
    if sample_size > len(raw_data):
        exc.raise_exception("The sample size cannot be larger than the original data length", ValueError) 

    sample_interval = len(raw_data) // sample_size            # 计算抽样间隔 
    start = random.randint(1, sample_interval); 
    sample_result = [];         

    for _ in range(sample_size):
        sample_result.append(raw_data[start-1]);
        start += sample_interval

    return sample_result; 



# 以主进程的方式运行 
if __name__ == "__main__":
    raw_data: dict = {}; 
    with open("./static/test_data.json", "r", encoding="utf-8") as file:
        raw_data: dict = json.load(file)["row_data"];  
        


    
