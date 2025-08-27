import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "C:/Users/ranje/OneDrive/Desktop/Customer Segmentation/CSV/customer_sales_cleaned_by_state.csv"
df = pd.read_csv(file_path)

# Display basic info
print("Original Data Shape:", df.shape)
print(df.head())

# Step 1: Select relevant numeric features for clustering
features = ['Age', 'LoyaltyPoints', 'UnitPrice', 'QuantitySold', 'Discount', 'TaxAmount', 'TotalSalesAmount', 'FinalAmount']
df_cluster = df[features]

# Step 2: Handle missing values if any
df_cluster.fillna(0, inplace=True)

# Step 3: Normalize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df_cluster)

# Step 4: Find optimal number of clusters using Elbow Method
inertia = []
k_range = range(1, 11)
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(scaled_data)
    inertia.append(km.inertia_)

plt.figure(figsize=(10, 5))
plt.plot(k_range, inertia, 'bo-')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal k')
plt.grid(True)
plt.show()

# Step 5: Apply KMeans with optimal number of clusters (e.g., k=4)
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_data)

# Step 6: Analyze the clusters
plt.figure(figsize=(10, 6))
sns.boxplot(x='Cluster', y='FinalAmount', data=df)
plt.title('FinalAmount Distribution Across Clusters')
plt.show()

# Save the updated DataFrame with cluster info
df.to_csv("C:/Users/ranje/OneDrive/Desktop/Customer Segmentation/CSV/customer_sales_cleaned_by_state1.csv", index=False)

print("Clustering completed and saved as 'customer_sales_clustered_data.csv'")
