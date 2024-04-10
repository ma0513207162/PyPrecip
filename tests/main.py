import pyprecip as precip 




if __name__ == "__main__": 
    csv_path = "./static/weather_data.csv"
    reader_list = precip.read_csv(csv_path)

    for item in reader_list:
        print(item)



