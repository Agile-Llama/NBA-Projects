To use these scripts. bbref-web-scraper.py will use an API to pull advanced stats/standard stats for a given NBA season. For example if you enter 1985 it will get the stats for 1984-85 season.

Saves this to a folder with a name you shouldn't change. Then run the script merge-datasets.py change the year in the script to the year which was entered in the bbred-we-scraper.py. This will take the 2 files created from the webscraper and merge it into 1. It will also remove those previous 2 files. 

The newly created file is now good to be used for the analysis scripts like pca-part2.py.