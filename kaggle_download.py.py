import os

# Set the path where you want to save the dataset
output_path = "./datasets"

# Download the dataset using os.system and Kaggle CLI
os.system(f"kaggle datasets download -d yaswanthgali/sport-celebrity-image-classification -p {output_path} --unzip")

print(f"Dataset downloaded to: {output_path}")
