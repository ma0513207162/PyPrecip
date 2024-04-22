import os, csv

def file_exists(func):
    def wrapper(*args, **kwargs):
        csv_path = args[0]
        if not os.path.exists(csv_path):
            raise FileExistsError(f"File '{csv_path}' does not exist")
        return func(*args, **kwargs)
    return wrapper



def excel_to_csv(excel_path: str) -> str:
    pass 

@file_exists
def read_excel(excel_path: str) -> list:
    reader_list:list = []

    with open(excel_path, "r") as excel_file:
        result = excel_file.read()
        print(result)


@file_exists
def read_csv(csv_path: str) -> list:
    reader_list: list = []

    with open(csv_path, "r") as csv_file:
        reader = csv.reader(csv_file)          
        reader_list = list(reader)
        
    return reader_list
    

if __name__ == "__main__": 
    csv_path = "./static/weather_data.csv"
    reader_list = read_csv(csv_path); 


    
    










    
   
    


    



    


