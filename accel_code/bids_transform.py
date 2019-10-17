"""
move/rename the raw datafiles to their respective
project folders with BIDS naming convention.
"""

from accel_code import utils
from bids import BIDSLayout
from bids.layout.writing import build_path
from bids.tests import get_test_data_path
import os

# This function takes in the old file name, information from redcap, and project name
# to return a bids formatted file name
def bids_transform(target_project, sub_id, ses_id):

    data_path = utils.get_test_data_path(target_project)

    if target_project == 'BETTER':
        sub_id = 'GE' + sub_id

    entities = {
    'subject': sub_id,
    'ses': ses_id,
    'suffix': 'accel',
    'extension': 'csv'
    }
    
    # This should give something like: sub-01/func/sub-01_ses-5_accel.csv
    new_file_name = build_path(entities, 'sub-{subject}/[ses-{ses}/]beh/sub-{subject}[_ses-{ses}]_{suffix}.{extension}')

    new_file_location = os.path.join(data_path, new_file_name)
    
    return(new_file_location)