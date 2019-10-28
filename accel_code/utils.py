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

bike_atrain_dict = {'161':'GEA161', '270':'GEA270', '290':'GEA290', '307':'GEA307',
    '311':'GEA311', '316':'GEA316', '351':'GEA351', '357':'GEA357', '383':'GEA383',
    '392':'GEA392', '457':'GEA457', '487':'GEA487', '514':'GEA514', '289':'GEP289',
    '291':'GEP291', '295':'GEP295', '326':'GEP326', '327':'GEP327', '360':'GEP360',
    '374':'GEP374', '381':'GEP381', '385':'GEP385', '472':'GEP472', '484':'GEP484',
    '511':'GEP511', '529':'GEP529', '142':'SEA142', '225':'SEA225', '228':'SEA228',
    '247':'SEA247', '1001':'SEH1001', '1002':'SEH1002', '1011':'SEA1011',
    '1015':'SEA1015', '1020':'SEH1020', '1028':'SEH1028', '1066':'SEH1066',
    '1086':'SEH1086', '015':'SEN015', '055':'SEN055', '075':'SEN075', '090':'SEN090',
    '202':'SEP202', '206':'SEP206', '223':'SEP223', '252':'SEP252'
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
    elif (project == 'BIKE-Pre') or (project == 'BIKE-Post'):
        bids_dir = os.path.join(
            'vosslabhpc',
            'Projects',
            project_dict[project]['vosslabhpc'],
            'Imaging',
            'BIDS')
    elif project == 'AMBI':
        bids_dir = os.path.join(
            'vosslabhpc',
            'Projects',
            project_dict[project]['vosslabhpc'],
            '3-Experiment',
            '2-Data',
            'Imaging',
            'BIDS')
    else:
        bids_dir = os.path.join(
            'vosslabhpc',
            'Projects',
            project_dict[project]['vosslabhpc'],
            '3-Experiment',
            '2-Data',
            'BIDS')

    return(bids_dir)
