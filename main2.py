import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the uploaded CSV file to check its contents
file_path = 'output.csv'
data = pd.read_csv(file_path)

# Display the first few rows to understand its structure
data = data.iloc[0:720 ,2:100]
print(data.head())



#Convert data to numeric format (if not already)
data_numeric = data.apply(pd.to_numeric, errors='coerce')

#Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(data_numeric, cmap='viridis', cbar=True)
plt.title("Heatmap of Lidar Data", fontsize=14)
plt.xlabel("Columns")
plt.ylabel("Rows")
plt.show()
