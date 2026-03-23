import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess



if len(sys.argv) < 2:
    sys.exit(1);

file_path = sys.argv[1]             #Read file path from command line FIRST
print(f"Creating drwawings for: {file_path}. ")
data = pd.read_csv(file_path);

numericalColumns = data.select_dtypes(include=['number']).columns.to_list();
fig, axis = plt.subplots(1, 3, figsize = (18, 5));  

if len(numericalColumns) >= 2:
    #histogram for numerical colmns only.
    axis[0].hist(data[numericalColumns[0]].dropna(), bins = 30, color = 'skyblue', edgecolor = 'black')
    axis[0].set_title(f"Histogram: {numericalColumns[0]}. ");

    #scatter plot for the first two numeric columns(if they exist) (the samples sat to 50,000 points to lower RAM usage). 
    sampleData = data.sample(n=min(50000, len(data)), random_state=2);
    axis[1].scatter(sampleData[numericalColumns[0]], sampleData[numericalColumns[1]], alpha = 0.5);
    axis[1].set_xlabel(numericalColumns[0])
    axis[1].set_ylabel(numericalColumns[1])
    axis[1].set_title("Scatter plot [Sampled]. ");


    #heatmap to show correlation between numeric columns
    corr = data[numericalColumns].corr()
    sns.heatmap(corr, ax=axis[2], cmap ='coolwarm');
    axis[2].set_title("Correlation heatmap. ");

#to save the image after plotting
plt.tight_layout()
plt.savefig("summary_plot.png");
print("Saved plots to the png file. ");

subprocess.run(['python', 'cluster.py', file_path]);