import sys
import pandas as pd

if len(sys.argv) < 2:
    print("Please provide a dataset file path.")
    sys.exit(1)

file_path = sys.argv[1]

try:
    data = pd.read_csv(file_path)
    
    data.to_csv('data_raw.csv', index=False)
    print("Dataset loaded and saved successfully as data_raw.csv")

except Exception as e:
    print(f"An error occurred: {e}")