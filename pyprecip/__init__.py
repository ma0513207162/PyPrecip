import os, csv 


def read_csv(csv_path):
    if not os.path.exists(csv_path):  
        raise FileExistsError

    reader_list: list = []; 
    with open(csv_path, "r") as csv_file:
        reader = csv.reader(csv_file)           # reader object 
        reader_list = list(reader)
        
    return reader_list 