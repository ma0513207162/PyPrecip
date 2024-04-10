import pandas as pd 
import os 


def read_excel(file_path):
    data = pd.read_excel(file_path)
    pass 

def read_csv(file_path):
    try:
        data = pd.read_csv(filepath_or_buffer = file_path, index_col=['日期', '时间'] ,encoding='gb18030' )
        result = data.loc["2023/3/1"]    
        return result.iterrows()

    except FileNotFoundError:
        print(f"文件 {file_path} 不存在")
    except PermissionError:
        print(f"无权限读取文件 {file_path}")
    except Exception as e:
        print(f"读取文件 {file_path} 时发生错误: {str(e)}")



if __name__ == "__main__": 
    file_path = "./static/weather_data.csv"
    read_result = read_csv(file_path)

    



    


