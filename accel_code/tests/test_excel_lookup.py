from datetime import datetime
import os

from ..excel_lookup import excel_lookup

@pytest.mark.parametrize("participant,expected_ses_id,expected_project,date_str",
                         [
                             ("45", "", "ALERT", "2016-03-19"),
                             ("157", "", "PACR", "2015-08-22"),
                             ("472", "", "Normative", "2015-07-29"),
                             ("512", "Pre", "Bike_Pre", "2015-08-08"),
                             ("176", "", "AMBI", "2017-06-23"),
                             ("517", "Post", "Bike_Post", "2015-12-16"),
                             ("78", "", "BETTER", "2018-07-20"),
                         ])
def test_excel_lookup(participant, expected_ses_id, expected_project, date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    file_dir = os.path.dirname(os.path.realpath(__file__))
    excel_file = os.path.join(file_dir, "data", "ActiGraph_analysis_summary.xlsx")
    ses_id, project = excel_lookup(participant, date, excel_file)

    assert ses_id == expected_ses_id
    assert project == expected_project
