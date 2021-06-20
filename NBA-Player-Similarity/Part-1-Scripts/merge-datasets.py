# This script will merge my three datasets into a single csv file which will be the basis of all other scripts.

import pandas as pd

# Three datasets to merge together
df_per_36 = pd.read_csv("Data/36-minutes.csv")
df_advanced = pd.read_csv("Data/advanced.csv")
df_extra = pd.read_csv("Data/extra.csv")

# Merge the three datasets together. Also drop the columns which aren't relevant to our goal.
# Refer 'Pre-processing: Data-cleaning' header in the readme for a full breakdown of what this function does.
def merge_clean(df_per_36, df_advanced, df_extra):
    df_per_36 = df_per_36.drop(['Age', 'Tm', 'G', 'GS', 'MP'], axis = 1)
    df_advanced = df_advanced.drop(['Rk', 'Age', 'Pos', 'Tm'], axis = 1)

    # Remove special characters
    df_per_36['Player'] = df_per_36.Player.str.replace('.','')
    df_per_36['PlayerAdvanced'] = df_advanced.PlayerAdvanced.str.replace('.','')


    # Merging 36_minutes.csv and advanced are easy. They are both from the same place so they match up well.
    # Merging extras.csv will be more annoying.
    df = pd.concat([df_per_36, df_advanced], axis=1)

    # Drop the duplicate of the player name. And the rank which isn't relevant.
    df = df.drop(['PlayerAdvanced', 'Rk'], axis = 1)

    # Merge based off a key. That key is the player name.
    final_merge = pd.merge(left=df, right=df_extra, left_on='Player', right_on='Player')

    # Drop the last few columns.
    final_merge = final_merge.drop(['Team', 'Season', 'Season Type', 'Games'], axis = 1)

    # add new data to df.
    final_merge = add_features(final_merge)

    # Remove all rows which have a Minutes per game of less then 28.5
    final_merge = final_merge.drop(final_merge[final_merge.MPG < 28.5].index)

    return final_merge


# Add two new features to the dataframe.  
# The first is Assist to turnover ratio. The second is minutes per game. 
def add_features(df):
    # Add assist to turnover
    df['A2TO'] = (df['TOV-per-36'] / df['AST-per-36'])

    # Add Minutes per game.
    df['MPG'] = (df['MP']/df['G'])

    return df
    

if __name__ == '__main__':
    df = merge_clean(df_per_36, df_advanced, df_extra) 
    df.to_csv('final.csv', index=False)

