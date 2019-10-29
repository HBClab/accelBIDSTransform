from datetime import datetime
import os
import pytest

from ..excel_lookup import excel_lookup


@pytest.mark.parametrize("participant,expected_ses_id,expected_project,date_str",
                         [
                             ("45", None, "ALERT", "2016-03-19"),
                             ("157", None, "PACR", "2015-08-22"),
                             ("472", None, "Normative", "2015-07-29"),
                             ("512", "pre", "Bike_Pre", "2015-08-08"),
                             ("176", None, "AMBI", "2017-06-23"),
                             ("517", "post", "Bike_Post", "2015-12-16"),
                             ("78", "pre", "BETTER", "2018-07-20"),
                             ("827", "3", "EXTEND", "2018-11-29"),
                         ])
def test_excel_lookup(participant, expected_ses_id, expected_project, date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    file_dir = os.path.dirname(os.path.realpath(__file__))
    excel_file = os.path.join(file_dir, "data", "ActiGraph_analysis_summary.xlsx")
    ses_id, project = excel_lookup(participant, date, excel_file)

    assert ses_id == expected_ses_id
    assert project == expected_project
