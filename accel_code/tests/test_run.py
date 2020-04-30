import os
import sys

import redcap

from .conftest import MockProject
from ..run import main


def test_main(monkeypatch):

    # patch the redcap project
    monkeypatch.setattr(redcap, "Project", MockProject)

    project_root_directory = os.path.join(
        os.path.dirname(__file__),
        'data',
        'vosslabhpc',
    )

    old_file_path = os.path.join(
        os.path.dirname(__file__),
        'data',
        '827 (2018-11-29)RAW.csv',
    )

    api_key = 'fake_api_key'

    excel_file_path = os.path.join(
        os.path.dirname(__file__),
        'data',
        'ActiGraph_analysis_summary.xlsx',
    )

    logging_directory = os.path.join(
        os.path.dirname(__file__),
        'data',
    )

    args = [
        "accel_transform",
        project_root_directory,
        old_file_path,
        api_key,
        excel_file_path,
        "--logging-directory", logging_directory,
        "--replace", "yes",
    ]

    # pass arguments to be parsed by main
    monkeypatch.setattr(sys, 'argv', args)

    assert main() is None
