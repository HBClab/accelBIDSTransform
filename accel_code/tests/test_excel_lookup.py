from datetime import datetime
import os

from ..excel_lookup import excel_lookup


def test_excel_lookup():
    participant = "827"
    expected_ses_id = "3"
    expected_project = "EXTEND"
    date = datetime.strptime("2018-11-29", "%Y-%m-%d")
    file_dir = os.path.dirname(os.path.realpath(__file__))
    excel_file = os.path.join(file_dir, "data", "ActiGraph_analysis_summary.xlsx")
    ses_id, project = excel_lookup(participant, date, excel_file)

    assert ses_id == expected_ses_id
    assert project == expected_project
