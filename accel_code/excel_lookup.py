"""
find project and session information
"""

import pandas as pd
from pandas import ExcelFile
from datetime import datetime

# This function returns the session id and project for a given lab id and date
def excel_lookup(lab_id, date, excel_file):
    
    df = pd.read_excel(excel_file)
    
    # convert all ID's to strings
    df.LabID = df.LabID.astype(str)
    sess = df[( df['LabID'].str.contains(sub_id) ) & ( df['File date'] == date )]
    sess_id = str(sess['LabID']).split('_')[1]
    project = str(sess['Project'])
    
    return sess_id, project