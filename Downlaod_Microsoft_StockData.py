import kagglehub

# Download latest version
path = kagglehub.dataset_download("varpit94/microsoft-stock-data")

print("Path to dataset files:", path)