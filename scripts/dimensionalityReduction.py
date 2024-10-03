import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('your_numerical_dataset.csv')

# Make data PCA standard
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Set n-components to None to keep all components. Change none to a number to keep that many components.
pca = PCA(n_components=None)

# Fit PCA on the scaled data
X_pca = pca.fit_transform(X_scaled)

# Examine the explained variance ratio to decide how many components to keep
explained_variance = pca.explained_variance_ratio_
print(f"Explained Variance Ratio: {explained_variance}")

# Choose the number of components to retain based on cumulative explained variance
cumulative_variance = np.cumsum(explained_variance)
print(f"Cumulative Explained Variance: {cumulative_variance}")

# Keep components that explain 95% of the variance
n_components_95 = np.argmax(cumulative_variance >= 0.95) + 1
print(f"Number of components to explain 95% variance: {n_components_95}")

# If desired, re-run PCA with the reduced number of components
pca_reduced = PCA(n_components=n_components_95)
X_pca_reduced = pca_reduced.fit_transform(X_scaled)