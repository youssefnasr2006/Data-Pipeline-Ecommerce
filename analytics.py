import sys
import pandas as pd
import subprocess

if len(sys.argv) < 2:
    sys.exit(1);

inputPath = sys.argv[1]
df = pd.read_csv(inputPath);

insight1 = f"Total valid records processed after cleaning: {len(df)}\n ";
insight2 = f"Number of features available for analysis: {len(df.columns)}\n";
insight3 = f"Statistical summary for the preprocessed numedical data: \n {df.describe().to_string()}\n";


with open("insight1.txt", "w") as f:
    f.write(insight1);

with open("insight2.txt", "w") as f:
    f.write(insight2);

with open("insight3.txt", "w") as f:
    f.write(insight3);


subprocess.run(["python", "visualize.py", inputPath]);