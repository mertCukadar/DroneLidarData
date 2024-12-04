import pandas as pd

# CSV dosyasını yükleyin
pathName = "LidarData.csv"
windowSize = 100
output_pd = pd.DataFrame()

data_csv_lidar = pd.read_csv(pathName)

# Toplam veri sayısını alın
total_rows = len(data_csv_lidar)

# 100'erlik pencere ile verileri işleme
for i in range(0, total_rows, windowSize):
    # Pencereyi alın
    window = data_csv_lidar[i:i + windowSize]

    # Pencerenin içeriğini işleyin
    filtered_df = window['Object Name'] == "wall"
    if(filtered_df.value_counts()[True] != 100):
        output_pd = pd.concat([output_pd , window] ,axis=0)


output_pd.to_csv("output.csv")



   