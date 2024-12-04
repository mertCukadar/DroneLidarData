import pandas as pd
import os

# CSV dosyasını yükleyin
pathName = "LidarData.csv"
windowSize = 30
output_pd = pd.DataFrame()

data_csv_lidar = pd.read_csv(pathName)

# Toplam veri sayısını alın
total_rows = len(data_csv_lidar)

for i in range(0, total_rows, windowSize):
    window = data_csv_lidar[i:i + windowSize]
    
    if len(window) == windowSize:
        is_blank = window.iloc[:, 103] == '  '
        values = window.iloc[:,103].unique()
        filtered_values = [val.strip() for val in values if val.strip() != '']
        if(filtered_values is not []):
            filename = f"{filtered_values}.csv" 

            if os.path.exists(filename):
                window.to_csv(filename, mode='a', index=False, header=False)
            else:
                window.to_csv(filename, index=False)
        
        if not is_blank.all():
            output_pd = pd.concat([output_pd, window], axis=0)


