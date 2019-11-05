"""
main file to transform raw data to BIDS files
"""

from accel_code import utils, redcap_query, excel_lookup, bids_transform
import argparse
from argparse import RawTextHelpFormatter


# This function builds a parser that allows this tool to be used
# from a CLI
def get_parser():
    parser = argparse.ArgumentParser(
                    description='accelBIDSTransform BIDS args',
                    formatter_class=RawTextHelpFormatter
                    )

    parser.add_argument('old_file_name',
                        help=('the name of the old accelerometer data file'
                              'which gets converted to BIDS format'))
    parser.add_argument('api_key',
                        help='the api key used to access redcap data')
    parser.add_argument('excel_file',
                        help=('location of the excel file containing the'
                              'Actigraph Summary'))

    return parser


def main():

    opts = get_parser().parse_args()

    lab_id = utils.get_lab_id(opts.old_file_name)
    date = utils.get_date(opts.old_file_name)

    ses_id, project = excel_lookup.excel_lookup(lab_id, date, opts.excel_file)

    sub_id = redcap_query.redcap_query(lab_id, project, opts.api_key)

    new_file_location = bids_transform.bids_transform(project, sub_id, ses_id)

    utils.make_directory(new_file_location)

    return


if __name__ == "__main__":
    main()
