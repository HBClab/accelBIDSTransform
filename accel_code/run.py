"""
main file to transform raw data to BIDS files
"""

from accel_code import utils, redcap_query, excel_lookup, bids_transform
import argparse
from argparse import RawTextHelpFormatter
import os


# This function builds a parser that allows this tool to be used
# from a CLI
def get_parser():
    parser = argparse.ArgumentParser(
                    description='accelBIDSTransform BIDS args',
                    formatter_class=RawTextHelpFormatter
                    )

    parser.add_argument('project_root_directory',
                        help=('location of the root directory containing the'
                              'project files'))
    parser.add_argument('old_file_name',
                        help=('the name of the old accelerometer data file'
                              'which gets converted to BIDS format'))
    parser.add_argument('api_key',
                        help='the api key used to access redcap data')
    parser.add_argument('excel_file',
                        help=('location of the excel file containing the'
                              'Actigraph Summary'))
    parser.add_argument('--replace', default='no',
                        choices=['yes', 'no'],
                        help='replace current output file')

    return parser


def main():

    opts = get_parser().parse_args()
    root = opts.project_root_directory

    lab_id = utils.get_lab_id(opts.old_file_name)
    date = utils.get_date(opts.old_file_name)

    ses_id, project = excel_lookup.excel_lookup(lab_id, date, os.path.join(root, opts.excel_file))

    sub_id = redcap_query.redcap_query(lab_id, project, opts.api_key)

    new_file_name = bids_transform.bids_transform(project, sub_id, ses_id)

    utils.make_directory(os.path.join(root, opts.old_file_name),
                         os.path.join(root, new_file_name), opts.replace)

    return


if __name__ == "__main__":
    main()
