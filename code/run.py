"""
main file to transform raw data to BIDS files
"""

import utils
import redcap_query
import excel_lookup
import bids_transform

def main():
    
    # Define file name here for initial test
    old_file_name = ''

    lab_id = utils.get_lab_id(old_file_name)
    date = utils.get_date(old_file_name)

    sess_id, project = excel_lookup.excel_lookup(lab_id, date)

    # Add api key to function definition prior to running
    sub_id = redcap_query.redcap_query(lab_id, project)

    new_file_location = bids_transform.bids_transform(project, sub_id, sess_id)

    return(new_file_location)

if __name__ == "__main__":
    main()