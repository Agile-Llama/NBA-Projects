import pandas as pd
import config
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

# https://github.com/Phlya/adjustText
from adjustText import adjust_text

year_to_load = '2004'

df = pd.read_csv('../Part-2-Data/%s_final.csv' % (year_to_load))

text = []

# Which of the three to run.
overall_impact = True
offensive_impact = False
defensive_impact = False

def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)


def player_impact(x, y, title):
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(x)
    principal_df = pd.DataFrame(data = principal_components , columns = ['principal component 1', 'principal component 2'])

    final_df = pd.concat([principal_df, df[['Pos']]], axis = 1)

    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_title('2 component PCA', fontsize = 20)
    targets = ['C', 'PF', 'PG', 'SF', 'SG']
    colors = ['r', 'g', 'b', 'c', 'm']

    for target, color in zip(targets, colors):
        indices_to_keep = final_df['Pos'] == target
        ax.scatter(final_df.loc[indices_to_keep, 'principal component 1'], final_df.loc[indices_to_keep, 'principal component 2'], c = color, s = 50, cmap=plt.cm.Blues)
    
    ax.legend(targets)
    ax.grid()

    label_point(final_df['principal component 1'], final_df['principal component 2'], df['Player'], ax)

    # Add the labels to the plots. Using a library which reduces overlapping.
    plt.title('(%s Interations) %s' % (adjust_text(text, arrowprops=dict(arrowstyle="-", color='k', lw=0.5), save_steps=False), title))

    plt.show()

# Function which annotates each point on the PCA plot with the players name. Currently just adds all to a list. 
# This list is used to add labels later without overlapping labels.
def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        #ax.text(point['x'], point['y']+0.1, str(point['val']))
        text.append(plt.text(point['x'], point['y'], str(point['val']), size=9))



if __name__ == '__main__':
    y = df['Pos']

    if overall_impact:
        x = df
        x = x.drop(['Pos','Player', 'G', 'MP', ], axis=1)
        x = clean_dataset(x)
        x = StandardScaler().fit_transform(x)
        player_impact(x, y, '%s Overall Player Impact' % (year_to_load))
