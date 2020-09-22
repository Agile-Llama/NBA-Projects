import pandas as pd
import config

# Break up into seperate files based off years. Create a file based off these years. 
# Used for when looking at Eras.
def seperate_by_years(year, end=None, save=False):
    """
    Function that will take the large dataset and get all the data for a given year. (Of a range of years.)
    Can save this data as a csv file with the file name being the year. ie 2013.csv.
    
    Args:
        year (int) : Year in which to get the stats for. if end isn't set to 'None' then use it as the start year for a range.
        end (opt, int) : The ending year in a range. ie get stats for 1979-1989.
        save (bool) : By default don't save. But if flag is True save it in the directory specified in the config file.
        
    Return:
        Returns a dataframe that has removed all the years which are not wanted.
    """

    # Import all into a pandas dataframe.
    dataframe = pd.read_csv(config.all_years_dataset, low_memory=False)
    
    if end != None:

        # Check that end is greater than the year.
        if end < year:
            print('End needs to be greater than the start year...')
        else:
            # Selecting a range of years.
            dataframe_seperated = dataframe.loc[dataframe['Year'] == year]
            for i in range(year+1, end+1):
                dataframe_seperated = dataframe_seperated.append(dataframe.loc[dataframe['Year'] == i])
                
    else:
        # Single year
        dataframe_seperated = dataframe.loc[dataframe['Year'] == year]

    # if save = True Then save the file as a csv file in the respective directory.
    if save:
        if end != None:
             # Save as range name ie 1979_1990.csv
            dataframe_seperated.to_csv('%s/%s.csv' % (config.folder_for_years, str(year)+'_'+str(end)))
        else:
            # Save as non range name ie 1979.csv
            dataframe_seperated.to_csv('%s/%s.csv' % (config.folder_for_years, str(year)))

    return dataframe_seperated

seperate_by_years(2001, save=True)

    