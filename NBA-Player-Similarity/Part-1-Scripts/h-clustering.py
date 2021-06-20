import scipy.cluster.hierarchy as shc
from matplotlib import pyplot as plt
import config
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.cluster import AgglomerativeClustering 

# Which of the three to run.
overall_impact = True
offensive_impact = False
defensive_impact = False

def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)

df = pd.read_csv(config.final_dataset)

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

pca = PCA(n_components=2)
principal_components = pca.fit_transform(x)
principal_df = pd.DataFrame(data = principal_components , columns = ['principal component 1', 'principal component 2'])

def cluster():

    # Set the title based off boolean
    if overall_impact:
        title = 'Overall Player Impact'
    elif offensive_impact:
        title = 'Offensive Player Impact'
    elif defensive_impact:
        title = 'Defensive Player Impact'

    plt.figure(figsize=(10, 7))  
    plt.title("%s Dendrogram" % (title))  

    labels = df['Player']
    labels_list = labels.to_list()

    dend = shc.dendrogram(shc.linkage(principal_components, method='weighted'), labels=labels_list, orientation='left')
    plt.show()

cluster()

