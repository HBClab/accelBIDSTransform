"""
find the participant_id given the lab_id and project_id
"""
import pandas as pd
from redcap import Project

# This function queries redcap to get the participant id from a given lab id and project name
def redcap_query(lab_number, project_name):
    
    api_url = 'https://redcap.icts.uiowa.edu/redcap/api/'
    # INSERT API KEY BELOW TO RUN
    api_key = ''
    project = Project(api_url, api_key)
    
    wanted_field_names = ['lab_id']
    wanted_field_names.append(project_name.lower() + '_id')

    sub_id_df = project.export_records(fields=wanted_field_names, format='df')
    participant_id = str( int( sub_id_df.loc[lab_number, wanted_field_names[1]] ) )
    
    return( participant_id )
