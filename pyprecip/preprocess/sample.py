import json, random;  
from ..utits.sundries import check_param_type
from ..utits.except_ import RaiseException as exc


# 分层系统抽样 
def stratify_system_sample():
    pass 

# 系统抽样 
def system_sample():
    pass 

# 分层采样 
def stratify_sample():
    pass 
  
# 简单随机选择 
def simple_random_sample(raw_data: list, sample_num: int, seed: int = None):
    """
    """
    check_param_type(raw_data, list, "raw_data");
    check_param_type(sample_num, int, "sample_num");
    check_param_type(seed, (int|None), "seed");

    if sample_num <= 0:
        exc.raise_exception("The sample size must be greater than 0", ValueError)
    if sample_num > len(raw_data):
        exc.raise_exception("The sample size cannot be larger than the original data length", ValueError)

    # 随机种子  
    if seed is not None: 
        random.seed(seed); 
    
    indices = list(range(len(raw_data)));
    random.shuffle(indices);   
    
    # 根据样本量获取对应索引的数据行
    sample_indices = indices[:sample_num]
    sample_result = [raw_data[i] for i in sample_indices]
    
    return sample_result; 


# 以主进程的方式运行 
if __name__ == "__main__":
    raw_data: dict = {}; 
    with open("./static/test_data.json", "r", encoding="utf-8") as file:
        raw_data: dict = json.load(file)["row_data"];  
        
    sample_result = simple_random_sample(raw_data, -1); 
    print(sample_result) 


