import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import config

df = pd.read_csv(config.final_dataset)

# Feature correlation. 
def correlation():
    corr = df.corr()

    fig, ax = plt.subplots(figsize=(24, 18))

    hm = sns.heatmap(corr, cbar=True, vmin=-1, vmax=1,
                 fmt='.2f', annot_kws={'size': 3}, annot=True, 
                 square=True, cmap=plt.cm.Blues)

    ticks = np.arange(corr.shape[0]) + 0.5
    ax.set_xticks(ticks)
    ax.set_xticklabels(corr.columns, rotation=90, fontsize=8)
    ax.set_yticks(ticks)
    ax.set_yticklabels(corr.index, rotation=360, fontsize=8)

    ax.set_title('correlation matrix')
    plt.tight_layout()
    plt.savefig("corr_matrix", dpi=300)

# Before doing the correlation drop the cols which we dont need.
df = df.drop(['Player', 'Pos', 'G', 'MP', 'Index'], axis=1)
correlation()