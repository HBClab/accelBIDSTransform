"""
helper functions
"""

from datetime import datetime
import re
import os

project_dict = {'EXTEND':{'redcap': 'extend_id', 'vosslabhpc': 'BikeExtend'},
    'BETTER':{'redcap': 'better_id', 'vosslabhpc': 'BETTER'},
    'BIKE_Post':{'redcap': 'bike_id', 'vosslabhpc': 'Bike_ATrain'},
    'BIKE_Pre':{'redcap': 'bike_id', 'vosslabhpc': 'Bike_ATrain'},
    'AMBI':{'redcap': 'ambi_id', 'vosslabhpc': 'AMBI'},
    'PACR':{'redcap': 'pacr_id', 'vosslabhpc': 'PACR-AD'},
    'ALERT':{'redcap': 'alertid', 'vosslabhpc': 'ALERT'},
    'Normative':{'redcap': 'normative_id', 'vosslabhpc': 'NormativeSample'}
}

# This function formats the date so it can be used in excel_lookup
def get_date(old_file_name):
    
    # Assume format <lab-id> (YYYY-MM-DD)RAW.csv
    date_extracted = re.search(r"\(.+\)", old_file_name).group(0)[1:-1]
    formatted_date = datetime.strptime(date_extracted, "%Y-%m-%d")
    return( formatted_date )

# This function extracts the lab id from the old accelerometer file naming scheme
def get_lab_id(old_file_name):
    return( old_file_name.split(' ')[0] )

# This function returns the root data path for storing project data
def get_test_data_path(project):

    if project == 'BETTER':
        bids_dir = os.path.join(
            'vosslabhpc',
            'Projects',
            project_dict[project]['vosslabhpc'],
            '3-Experiment',
            '2-data',
            'bids')
    else:
        bids_dir = os.path.join(
            'vosslabhpc',
            'Projects',
            project_dict[project]['vosslabhpc'],
            '3-Experiment',
            '2-Data',
            'BIDS')

    return(bids_dir)
