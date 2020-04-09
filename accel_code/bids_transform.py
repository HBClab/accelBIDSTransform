"""
move/rename the raw datafiles to their respective
project folders with BIDS naming convention.
"""

from accel_code import utils
from bids.layout.writing import build_path
import os


# This function takes in the old file name, information from redcap,
# and project name to return a bids formatted file name
def bids_transform(target_project, sub_id, ses_id):

    data_path = utils.get_test_data_path(target_project)

    if target_project == 'EXTEND':
        new_file_name = build_path(
            utils.get_bids_entities(sub_id, ses_id),
            ('sub-{subject}/[ses-accel{ses}/]beh/sub-{subject}'
                '[_ses-accel{ses}]_{suffix}.{extension}')
            )

    elif target_project == 'BETTER':
        sub_id = 'GE' + sub_id
        new_file_name = build_path(
            utils.get_bids_entities(sub_id, ses_id),
            ('sub-{subject}/[ses-{ses}/]beh/sub-{subject}'
                '[_ses-{ses}]_{suffix}.{extension}')
            )

    elif (target_project == 'BIKE_Pre') or (target_project == 'BIKE_Post'):
        sub_id = utils.bike_atrain_dict[sub_id]
        new_file_name = build_path(
            utils.get_bids_entities(sub_id, ses_id),
            ('sub-{subject}/[ses-{ses}/]beh/sub-{subject}'
                '[_ses-{ses}]_{suffix}.{extension}')
            )

    elif target_project == 'PACR':
        sub_id = utils.pacr_dict[sub_id]
        new_file_name = build_path(
            utils.get_bids_entities(sub_id, ses_id),
            ('sub-{subject}/[ses-{ses}/]beh/sub-{subject}'
                '[_ses-{ses}]_{suffix}.{extension}')
            )

    else:
        # This should give: sub-01/ses-5/beh/sub-01_ses-5_accel.csv

        # If there is a new/unknown project, the accelBIDSTransform tool will 
        # return only the file name with no additional data_path for the project
        # To add new project information, add a conditional above this and modify
        # the utils.py file to account for a new data_path
        new_file_name = build_path(
            utils.get_bids_entities(sub_id, ses_id),
            ('sub-{subject}/[ses-{ses}/]beh/sub-{subject}'
                '[_ses-{ses}]_{suffix}.{extension}')
            )

    new_file_location = os.path.join(data_path, new_file_name)

    return(new_file_location)
