import pandas as pd

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
        
        print(is_blank)
        if not is_blank.all():
            output_pd = pd.concat([output_pd, window], axis=0)

# Sonuçları kaydet
output_pd.to_csv("output.csv", index=False)
