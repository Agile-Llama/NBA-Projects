import pandas as pd
import config
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

df = pd.read_csv(config.final_dataset)

y = df['Pos']

x = df
x = x.drop(['Pos','Player', 'G', 'MP', 'Index'], axis=1)

x = StandardScaler().fit_transform(x)

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents , columns = ['principal component 1', 'principal component 2'])

finalDf = pd.concat([principalDf, df[['Pos']]], axis = 1)

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = ['C', 'PF', 'PG', 'SF', 'SG']
colors = ['r', 'g', 'b', 'c', 'm']

for target, color in zip(targets,colors):
    indicesToKeep = finalDf['Pos'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'], finalDf.loc[indicesToKeep, 'principal component 2'], c = color, s = 50)
    
    # ax.text(finalDf.loc[indicesToKeep, 'principal component 1'], finalDf.loc[indicesToKeep, 'principal component 2'], s='hello', fontsize=10)

ax.legend(targets)
# ax.grid()

def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x'], point['y']+0.1, str(point['val']))

label_point(finalDf['principal component 1'], finalDf['principal component 2'], df['Player'], ax)


plt.show()