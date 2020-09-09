# This script will merge my three datasets into a single csv file which will be the basis of all other scripts.

import pandas as pd

# Three datasets to merge together
df_per_36 = pd.read_csv("Data/36-minutes.csv")
df_advanced = pd.read_csv("Data/advanced.csv")
df_extra = pd.read_csv("Data/extra.csv")

# Merge the three datasets together. Also drop the columns which aren't relevant to our goal.
def merge(df_per_36, df_advanced, df_extra):
    df_per_36 = df_per_36.drop(['Age', 'Tm', 'G', 'GS', 'MP'], axis = 1)
    df_advanced = df_advanced.drop(['Rk', 'Age', 'G', 'MP', 'Pos', 'Tm'], axis = 1)

    # Merging 36_minutes.csv and advanced are easy. They are both from the same place so they match up well.
    # Merging extras.csv will be more annoying.
    df = pd.concat([df_per_36, df_advanced], axis=1)

    # Drop the duplicate of the player name. And the rank which isn't relevant.
    df = df.drop(['Player-Advanced', 'Rk'], axis = 1)

    # Merge based off a key. That key is the player name.
    final_merge = pd.merge(left=df, right=df_extra, left_on='Player', right_on='Player')

    # Drop the last few columns.
    final_merge = final_merge.drop(['Team', 'Season', 'Season Type', 'Games'], axis = 1)

    return final_merge

if __name__ == '__main__':
    df = merge(df_per_36, df_advanced, df_extra)  
    df.to_csv('Data/final.csv') 

