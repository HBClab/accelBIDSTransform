"""
helper functions
"""

from datetime import datetime
import re
import os

# This function formats the date so it can be used in excel_lookup
def get_date(old_file_name):
    
    # Assume format <lab-id> (YYYY-MM-DD)RAW.csv
    date_extracted = re.search(r"\(.+\)", old_file_name).group(0)[1:-1]
    year_month_day = date_extracted.split('-')
    formatted_date = datetime(int(year_month_day[0]), int(year_month_day[1]), int(year_month_day[2]))
    return( formatted_date )

# This function extracts the lab id from the old accelerometer file naming scheme
def get_lab_id(old_file_name):
    return( old_file_name.split(' ')[0] )

# This function returns the root data path for storing project data
def get_test_data_path(project):
    project_dir = os.path.join('\\vosslabhpc\Projects', project)
    exp_dir = os.path.join(project_dir, '3-Experiment')
    data_dir = os.path.join(exp_dir, '2-data')
    bids_dir = os.path.join(data_dir, 'bids')
    return(bids_dir)
