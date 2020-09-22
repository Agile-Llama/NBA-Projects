import pandas as pd
import config

year_to_load = '2001'

df_standard = pd.read_csv(config.folder_for_years+"/%s_player_s_totals.csv" % (str(year_to_load)))
df_advanced = pd.read_csv(config.folder_for_years+"/%s_adv_player_s_totals.csv" % (str(year_to_load)))

# Add two new features to the dataframe.  
# The first is Assist to turnover ratio. The second is minutes per game. 
def add_features(df):
    # Add assist to turnover
    # df['A2TO'] = (df['TOV-per-36'] / df['AST-per-36'])

    # Add Minutes per game.
    df['MPG'] = (df['minutes_played']/df['games_played'])

    return df


def merge_clean(df_standard, df_advanced):
    df_standard = df_standard.drop(['slug', 'age', 'team'], axis = 1)
    df_advanced = df_advanced.drop(['slug', 'age', 'team', 'positions'], axis = 1)

    # Remove special characters
    df_standard['name'] = df_standard.name.str.replace('.','')
    df_advanced['name'] = df_advanced.name.str.replace('.','')

    df = pd.merge(left=df_standard, right=df_advanced, left_on='name', right_on='name')

    df = df.drop(['is_combined_totals', 'value_over_replacement_player'], axis=1)

    df['MPG'] = (df['minutes_played_x']/df['games_played_x'])

    df = df.drop(df[df.MPG < 28.5].index)

    # Remove duplicate names tomorrow.

    return df

if __name__ == '__main__':
    df = merge_clean(df_standard, df_advanced) 
    df.to_csv('final-old.csv', index=False)