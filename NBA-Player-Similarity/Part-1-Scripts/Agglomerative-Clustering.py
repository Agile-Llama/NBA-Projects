import scipy.cluster.hierarchy as shc
from matplotlib import pyplot as plt
import config
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.cluster import AgglomerativeClustering 
from scipy.cluster.hierarchy import dendrogram

# Which of the three to run.
overall_impact = True
offensive_impact = False
defensive_impact = False

df = pd.read_csv(config.final_dataset)

def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)

def plot_dendrogram(model, **kwargs):
    # Children of hierarchical clustering
    children = model.children_

    # Distances between each pair of children
    # Since we don't have this information, we can use a uniform one for plotting
    distance = np.arange(children.shape[0])

    # The number of observations contained in each cluster level
    no_of_observations = np.arange(2, children.shape[0]+2)

    # Create linkage matrix and then plot the dendrogram
    linkage_matrix = np.column_stack([children, distance, no_of_observations]).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs, orientation='left')

if overall_impact:
    x = df
    x = x.drop(['Pos','Player', 'G', 'MP', 'Index', ], axis=1)
    x = clean_dataset(x)
    x = StandardScaler().fit_transform(x)

elif offensive_impact:
    x = df[['FG', 'G', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'FT', 'FTA', 'FT%',
        'TRB', 'BLK', 'A2TO', 'PTS', 'PER', 'TS%', '3PAr', 'DRB%', 'AST%', 'STL%', 'BLK%', 'BPM', 'VORP', 
        'Fast Break Pts', 'Points In Paint', 'Points off TO', 'Points scored per shot']]

    x = clean_dataset(x)
    x = StandardScaler().fit_transform(x)

elif defensive_impact:
    x = df[['ORB', 'AST', 'STL', 'FTr', 'TOV%', 'TRB%', 'AST%', 'USG%', 'WS/48']]
    x = clean_dataset(x)
    x = StandardScaler().fit_transform(x)


model = AgglomerativeClustering(n_clusters=3)

labels = df['Player']
labels_list = labels.to_list()

model = model.fit(x)
plt.title('Hierarchical Clustering Dendrogram')
plot_dendrogram(model, labels=labels_list)
plt.show()