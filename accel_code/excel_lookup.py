"""
find project and session information
"""

import pandas as pd
from pandas import ExcelFile
from datetime import datetime
import os

# This function returns the session id and project for a given lab id and date
def excel_lookup(lab_id, date, excel_file):
    
    df = pd.read_excel(excel_file)
    
    # convert all ID's to strings
    df.LabID = df.LabID.astype(str)
    
    try:
        ses = df[( df['LabID'].str.contains(lab_id) ) & ( df['File date'] == date )]
        
        # Check to make sure no labid/date combination gives more than one result
        if len(ses.index) > 1:
            raise IndexError("{lab_id}: {date} has multiple entries in excel file".format(lab_id=lab_id, date=date))
        
        project = str(ses['Project'].values)[2:-2]

        if project == 'EXTEND':
            ses_id = str(ses['LabID'].values[0].split('_')[1])

        elif project == 'BIKE-Pre':
            ses_id = 'pre'

        elif project == 'BIKE-Post':
            ses_id = 'post'

        elif project == 'BETTER':
            # All accelerometer data is stored in pre directory for this study
            ses_id = 'pre'

        elif project == 'AMBI':
            ses_id = None

        elif project == 'PACR':
            ses_id = None

        elif project == 'ALERT':
            ses_id = None

        elif project == 'Normative':
            ses_id = None
    
    except:
        raise ValueError("{lab_id}: {date} is not found in excel file".format(lab_id=lab_id, date=date))
    
    return ses_id, project