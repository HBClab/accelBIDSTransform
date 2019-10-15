"""
main file to transform raw data to BIDS files
"""

from accel_code import utils, redcap_query, excel_lookup, bids_transform
import json

def main():

    # Define variables here to run
    old_file_name = ''
    excel_file = ''
    api_key = ''

    lab_id = utils.get_lab_id(old_file_name)
    date = utils.get_date(old_file_name)

    sess_id, project = excel_lookup.excel_lookup(lab_id, date, excel_file)

    # Add api key to function definition prior to running
    sub_id = redcap_query.redcap_query(lab_id, project, api_key)

    new_file_location = bids_transform.bids_transform(project, sub_id, sess_id)

    return(new_file_location)


if __name__ == "__main__":
    main()
