import sys
import pandas as pd
import subprocess
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA

if len(sys.argv) < 2:
    sys.exit(1);

input_path = sys.argv[1]#reading symbol (1). 
df = pd.read_csv(input_path);

df = df.dropna();
df = df.drop_duplicates();

numericalColumns = df.select_dtypes(include=['number']).columns.tolist();
categoricalColumns = df.select_dtypes(exclude=['number']).columns.tolist();

if numericalColumns:
    scaler = StandardScaler()
    df[numericalColumns] = scaler.fit_transform(df[numericalColumns])

lEncoder = LabelEncoder()

for col in categoricalColumns:
    df[col] = lEncoder.fit_transform(df[col].astype(str));#converts to string. 


if numericalColumns:
    targetColumn = numericalColumns[0]
    df[f"{targetColumn}_binned"] = pd.qcut(df[targetColumn], q = 3, labels=['Low', 'Medium', 'High'], duplicates='drop')
    df[f"{targetColumn}_binned"] = lEncoder.fit_transform(df[f"{targetColumn}_binned"].astype(str));


if len(numericalColumns) >= 2:
    pca = PCA(n_components=2);
    pcaFeatures = pca.fit_transform(df[numericalColumns]);
    df['pca1'] = pcaFeatures[:, 0];
    df['pca2'] = pcaFeatures[:, 1];


outputPath = "data_preprocessed.csv"

df.to_csv(outputPath, index=False)

subprocess.run(["python", "analytics.py", outputPath]);