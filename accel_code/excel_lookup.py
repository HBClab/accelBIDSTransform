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
    sess = df[( df['LabID'].str.contains(lab_id) ) & ( df['File date'] == date )]
    sess_id = str(sess['LabID'].values[0].split('_')[1])
    project = str(sess['Project'].values)[2:-2]
    
    return sess_id, project