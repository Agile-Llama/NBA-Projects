import pandas as pd
import config
import os

# Note if the year is 1985 that means its the 1984-85 season.
year_to_load = '2004'

df_standard = pd.read_csv(config.folder_for_years+"/%s_player_s_totals.csv" % (str(year_to_load)))
df_advanced = pd.read_csv(config.folder_for_years+"/%s_adv_player_s_totals.csv" % (str(year_to_load)))

os.remove(config.folder_for_years+"/%s_player_s_totals.csv" % (str(year_to_load)))
os.remove(config.folder_for_years+"/%s_adv_player_s_totals.csv" % (str(year_to_load)))

def merge_clean(df_standard, df_advanced):
    df_standard = df_standard.drop(['slug', 'age', 'team'], axis = 1)
    df_advanced = df_advanced.drop(['slug', 'age', 'team', 'positions'], axis = 1)

    # Remove special characters
    # df_standard['name'] = df_standard.name.str.replace('.','')
    # df_advanced['name'] = df_advanced.name.str.replace('.','')

    # Merge both datasets (ie advanced and standard) with each other with the name of the player as the key.
    df = pd.merge(left=df_standard, right=df_advanced, left_on='name', right_on='name')

    df = df.drop(['is_combined_totals', 'value_over_replacement_player', 'games_played_y', 'minutes_played_y'], axis=1)

    df['MPG'] = (df['minutes_played_x']/df['games_played_x'])

    # Drop all rows where the player doesn't have at least 28.5 MPG (Minutes per game)
    df = df.drop(df[df.MPG < 28.5].index)

    # Change the names of the positions to be better for plotting purposes
    mapping_positions = {'CENTER': 'C', 'SMALL FORWARD': 'SF', 'SHOOTING GUARD': 'SG', 'POINT GUARD': 'PG', 'POWER FORWARD': 'PF'}
    df = df.replace({'positions': mapping_positions})

    # Remove duplicate names.
    df = df.drop_duplicates(subset="name", keep="first")

    return df

# Function to calculate per 36 statistics for all players.
# The calculation for per 36 is to divide 36 by the number of minutes the player played.
# Then using this number on the statistic we want to standardize.
def calculate_per_36(df):
    to_standardize = list(['made_field_goals', 'attempted_field_goals', 'made_three_point_field_goals', 'attempted_three_point_field_goals', 'made_free_throws', 'attempted_free_throws', 'offensive_rebounds', 'defensive_rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'personal_fouls', 'points'])
    all_names = list(df.name.values.tolist()) 

    for name in all_names:
        for attribute in to_standardize:
            standardize_number = df.loc[df['name'] == name, 'minutes_played_x']
            attribute_number = df.loc[df['name'] == name, attribute]
            df.loc[df['name'] == name, attribute] = attribute_number*(36/standardize_number)

# Rename the column names to be more inline with part 1.
# No real reason other then makes it easier and cleaner to call in future.
def rename_cols(df):
    df.columns = ['Player', 'Pos', 'G', 'GS','MP', 'FG', 'FGA', '3P', '3PA', 'FT', 'FTA', 
    'ORB', 'DRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PER', 'TS%', '3PAr', 'FTr', 
    'ORB%', 'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS', 'DWS', 'WS', 
    'WS/48', 'OBPM', 'DBPM', 'BPM', 'MPG']

    return df


if __name__ == '__main__':
    df = merge_clean(df_standard, df_advanced) 

    # Standardize the relevant data points
    calculate_per_36(df)

    df = rename_cols(df)
    df.to_csv('../Part-2-Data/%s_final.csv' % (year_to_load), index=False)