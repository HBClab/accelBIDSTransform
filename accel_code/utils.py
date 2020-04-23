"""
helper functions
"""

from datetime import datetime
import re
import os
from shutil import copyfile

project_dict = {'EXTEND': {'redcap': 'extend_id', 'vosslabhpc': 'BikeExtend'},
                'BETTER': {'redcap': 'better_id', 'vosslabhpc': 'BETTER'},
                'BIKE_Post': {'redcap': 'bike_id',
                              'vosslabhpc': 'Bike_ATrain'},
                'BIKE_Pre': {'redcap': 'bike_id', 'vosslabhpc': 'Bike_ATrain'},
                'AMBI': {'redcap': 'ambi_id', 'vosslabhpc': 'AMBI'},
                'PACR': {'redcap': 'pacr_id', 'vosslabhpc': 'PACR-AD'},
                'ALERT': {'redcap': 'alertid', 'vosslabhpc': 'ALERT'},
                'Normative': {'redcap': 'normative_id',
                              'vosslabhpc': 'NormativeSample'}
                }

bike_atrain_dict = {'161': 'GEA161', '270': 'GEA270', '290': 'GEA290',
                    '307': 'GEA307', '311': 'GEA311', '316': 'GEA316',
                    '351': 'GEA351', '357': 'GEA357', '383': 'GEA383',
                    '392': 'GEA392', '457': 'GEA457', '487': 'GEA487',
                    '514': 'GEA514', '289': 'GEP289', '291': 'GEP291',
                    '295': 'GEP295', '326': 'GEP326', '327': 'GEP327',
                    '360': 'GEP360', '374': 'GEP374', '381': 'GEP381',
                    '385': 'GEP385', '472': 'GEP472', '484': 'GEP484',
                    '511': 'GEP511', '529': 'GEP529', '142': 'SEA142',
                    '225': 'SEA225', '228': 'SEA228', '247': 'SEA247',
                    '1001': 'SEH1001', '1002': 'SEH1002', '1011': 'SEA1011',
                    '1015': 'SEA1015', '1020': 'SEH1020', '1028': 'SEH1028',
                    '1066': 'SEH1066', '1086': 'SEH1086', '15': 'SEN015',
                    '55': 'SEN055', '75': 'SEN075', '90': 'SEN090',
                    '202': 'SEP202', '206': 'SEP206', '223': 'SEP223',
                    '252': 'SEP252'
                    }

pacr_dict = {'140': 'controlGE140', '154': 'controlGE154',
             '159': 'controlGE159', '161': 'controlGE161',
             '164': 'controlGE164', '166': 'controlGE166',
             '185': 'controlGE185', '190': 'controlGE190',
             '197': 'controlGE197', '204': 'controlGE204',
             '206': 'controlGE206', '6': 'controlSE006',
             '7': 'controlSE007', '13': 'controlSE013',
             '24': 'controlSE024', '31': 'controlSE031',
             '39': 'controlSE039', '44': 'controlSE044',
             '45': 'controlSE045', '51': 'controlSE051',
             '52': 'controlSE052', '65': 'controlSE065',
             '76': 'controlSE076', '78': 'controlSE078',
             '83': 'controlSE083', '86': 'controlSE086',
             '87': 'controlSE087', '92': 'controlSE092',
             '104': 'controlSE104', '113': 'controlSE113',
             '5': 'experimentalGE005', '132': 'experimentalGE132',
             '136': 'experimentalGE136', '146': 'experimentalGE146',
             '158': 'experimentalGE158', '174': 'experimentalGE174',
             '176': 'experimentalGE176', '178': 'experimentalGE178',
             '182': 'experimentalGE182', '191': 'experimentalGE191',
             '195': 'experimentalGE195', '199': 'experimentalGE199',
             '209': 'experimentalGE209', '8': 'experimentalSE008',
             '9': 'experimentalSE009', '10': 'experimentalSE010',
             '11': 'experimentalSE011', '12': 'experimentalSE012',
             '25': 'experimentalSE025', '43': 'experimentalSE043',
             '55': 'experimentalSE055', '56': 'experimentalSE056',
             '66': 'experimentalSE066', '74': 'experimentalSE074',
             '77': 'experimentalSE077', '89': 'experimentalSE089',
             '98': 'experimentalSE098', '102': 'experimentalSE102',
             '110': 'experimentalSE110'
             }


# This function returns the entities needed for the build_path function
def get_bids_entities(sub_id, ses_id):
    entities = {
        'subject': sub_id,
        'ses': ses_id,
        'suffix': 'accel',
        'extension': 'csv'
        }

    return entities


# This function adjusts subject id's for AMBI so they match vosslabhpc
def ambi_adjust(sub_id):
    if len(str(sub_id)) == 1:
        return '00' + sub_id

    elif len(str(sub_id)) == 2:
        return '0' + sub_id


# This function formats the date so it can be used in excel_lookup
def get_date(old_file_path):
    old_file_name = os.path.basename(old_file_path)
    # Assume format <lab-id> (YYYY-MM-DD)RAW.csv
    date_extracted = re.search(r"\(.+\)", old_file_name).group(0)[1:-1]
    formatted_date = datetime.strptime(date_extracted, "%Y-%m-%d")
    return(formatted_date)


# This function extracts the lab id from the old accelerometer file name
def get_lab_id(old_file_path):
    old_file_name = os.path.basename(old_file_path)
    return(int(old_file_name.split(' ')[0]))


# This function returns the root data path for storing project data
def get_test_data_path(project):

    if project == 'BETTER':
        bids_dir = os.path.join(
            'Projects',
            project_dict[project]['vosslabhpc'],
            '3-Experiment',
            '2-data',
            'bids')
    elif project == 'EXTEND':
        bids_dir = os.path.join(
            'Projects',
            project_dict[project]['vosslabhpc'],
            '3-Experiment',
            '2-Data',
            'BIDS')
    elif (project == 'BIKE_Pre') or (project == 'BIKE_Post'):
        bids_dir = os.path.join(
            'Projects',
            project_dict[project]['vosslabhpc'],
            'Imaging',
            'BIDS')
    elif project == 'AMBI':
        bids_dir = os.path.join(
            'Projects',
            project_dict[project]['vosslabhpc'],
            '3-Experiment',
            '2-Data',
            'Imaging',
            'BIDS')
    elif project == 'PACR':
        bids_dir = os.path.join(
            'Projects',
            project_dict[project]['vosslabhpc'],
            'Imaging',
            'BIDS')
    else:
        # Path doesn't exist
        bids_dir = os.path.join(
            'Projects',
            project_dict[project]['vosslabhpc'],
            '3-Experiment',
            '2-Data',
            'BIDS')

    return(bids_dir)


# This function makes the bids-formatted directory for the accelerometer file
def make_directory(old_path, new_path, replace):
    if os.path.exists(new_path):
        if replace == 'no':
            raise ValueError('replace option was not specified and output file exists', new_path)
        if replace == 'yes':
            os.remove(new_path)
            copyfile(old_path, new_path)
    else:
        os.makedirs(os.path.dirname(new_path))
        copyfile(old_path, new_path)
