from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import config

# Run this file for 2 datasets then merge them with another script.

# https://github.com/jaebradley/basketball_reference_web_scraper

# Advanced and Normal season totals for all players.
def get_season_totals(year):
    client.players_season_totals(
        season_end_year = year, 
        output_type=OutputType.CSV, 
        output_file_path=(config.folder_for_years+"/%s_player_s_totals.csv" % (str(year))) 
    )

    client.players_advanced_season_totals(
        season_end_year = year,
        output_type=OutputType.CSV, 
        output_file_path=(config.folder_for_years+"/%s_adv_player_s_totals.csv" % (str(year))) 
    )

if __name__ == '__main__':
    year = input('Enter Year: ')
    get_season_totals(int(year))