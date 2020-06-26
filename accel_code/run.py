"""
main file to transform raw data to BIDS files
"""

from accel_code import utils, redcap_query, excel_lookup, bids_transform
import argparse
from argparse import RawTextHelpFormatter
import os
import logging


# This function builds a parser that allows this tool to be used
# from a CLI
def get_parser():
    parser = argparse.ArgumentParser(
                    description='accelBIDSTransform BIDS args',
                    formatter_class=RawTextHelpFormatter
                    )

    parser.add_argument('project_root_directory',
                        help=('mount point of the vosslabhpc (root) directory containing the'
                              'project files'))
    parser.add_argument('old_file_path',
                        help=('the path of the old accelerometer data file'
                              'which gets converted to BIDS format'))
    parser.add_argument('api_key',
                        help='the api key used to access redcap data')
    parser.add_argument('excel_file_path',
                        help=('location of the excel file containing the'
                              'Actigraph Summary'))
    parser.add_argument('--replace', default='no',
                        choices=['yes', 'no'],
                        help='replace current output file')
    parser.add_argument('--logging-directory',
                        help='directory to place logging files')

    return parser


def main():

    opts = get_parser().parse_args()
    root = opts.project_root_directory

    logging_directory = opts.logging_directory if opts.logging_directory else os.getcwd()

    # assume we can get lab_id and date for the log file
    lab_id = utils.get_lab_id(opts.old_file_path)
    date = utils.get_date(opts.old_file_path)

    # set up the logging configuration
    logging_fname = '_'.join([str(lab_id), str(date.date())]) + '.log'
    logging_path = os.path.join(logging_directory, logging_fname)

    logger = logging.getLogger(__name__)
    logger.level = 10
    # create file handler which logs even debug messages
    fh = logging.FileHandler(logging_path)
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    # get session and project information
    try:
        ses_id, project = excel_lookup.excel_lookup(lab_id, date, opts.excel_file_path)
    except Exception as e:
        logger.exception("could not lookup {} ({}) in {}".format(
            lab_id, str(date), opts.excel_file_path))
        raise(e)

    # find subject id from redcap
    try:
        sub_id = redcap_query.redcap_query(lab_id, project, opts.api_key)
    except Exception as e:
        msg = "could not get subject id from redcap for {} ({})"
        logger.exception(msg.format(lab_id, str(date)))
        raise(e)
    # create a new path/filename using this information
    try:
        new_file_name = bids_transform.bids_transform(project, sub_id, ses_id)
    except Exception as e:
        msg = "could not create new filename: {} ({})"
        logger.exception(msg.format(lab_id, str(date)))
        raise(e)

    new_file_path = os.path.join(root, new_file_name)

    # copy the file to the new project specific location
    try:
        file_copied = utils.make_directory(opts.old_file_path, new_file_path, opts.replace)
    except Exception as e:
        msg = "could not copy file: {} ({})"
        logger.exception(msg.format(lab_id, str(date)))
        raise(e)
    
    if file_copied:
        logger.info("{of} -> {nf}".format(of=opts.old_file_path, nf=new_file_path))

    return


if __name__ == "__main__":
    main()
