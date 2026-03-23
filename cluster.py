import sys
import pandas as pd
from sklearn.cluster import KMeans


if len(sys.argv) < 2:
    sys.exit(1);

file_path = sys.argv[1]

df = pd.read_csv(file_path);
dfSampled = df.sample(n=min(100000, len(df)), random_state=42)

dfNumerical = dfSampled.select_dtypes(include=['number']).dropna()

if not dfNumerical.empty:
    #applying Kmeans 
    kmeans = KMeans(n_clusters= 3 , random_state=42, n_init='auto')#mute warnings
    clusters = kmeans.fit_predict(dfNumerical);


    #counting the samples in each cluster
    counts=  pd.Series(clusters).value_counts().sort_index()

    with open("clusters.txt", "w") as f:
        f.write("Kmeans clustering result with k = 3: \n");
        for clusterId, count in counts.items():
            f.write(f"Cluster {clusterId}: {count} samples\n");

    print("Clustring done and saved to cluster.txt. ");

