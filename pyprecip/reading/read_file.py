import os, csv

# decorator
def file_exists(func):
    def wrapper(*args, **kwargs):
        csv_path = args[0]
        if not os.path.exists(csv_path):
            raise FileExistsError(f"File '{csv_path}' does not exist")
        return func(*args, **kwargs)
    return wrapper



@file_exists
def read_csv(csv_path: str) -> list:
    reader_list: list = []

    with open(csv_path, "r") as csv_file:
        reader = csv.reader(csv_file)           # reader object 
        reader_list = list(reader)
        
    return reader_list



@file_exists
def read_excel(excel_path: str) -> list:
    reader_list:list = []

    with open(excel_path, "r") as excel_file:
        result = excel_file.read()
        print(result)



if __name__ == "__main__": 
    csv_path = "./static/weather_data2.csv"
    print(read_csv(csv_path))










    
   
    


    



    


