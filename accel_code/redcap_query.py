"""
find the subject_id given the lab_id and project_id
"""
import pandas as pd
import redcap
from accel_code import utils

# This function queries redcap to get the participant id from a given lab id and project name
def redcap_query(lab_number, project_name, api_key):
    
    api_url = 'https://redcap.icts.uiowa.edu/redcap/api/'

    project = redcap.Project(api_url, api_key)
    
    wanted_field_names = ['lab_id']
    wanted_field_names.append(utils.project_dict[project_name]['redcap'])

    sub_id_df = project.export_records(fields=wanted_field_names, format='df')
    subject_id = str( int( sub_id_df.loc[lab_number, wanted_field_names[1]] ) )
    
    return( subject_id )
