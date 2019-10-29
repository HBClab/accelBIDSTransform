import os
import pandas as pd
import redcap
import pytest

from ..redcap_query import redcap_query


class MockProject:

    def __init__(self, url, key):
        pass

    @staticmethod
    def export_records(fields, records=None, format='df'):
        test_path = os.path.dirname(os.path.realpath(__file__))
        if "extend_id" in fields:
            mock_file = "mock_redcap_extend.tsv"
        elif "better_id" in fields:
            mock_file = "mock_redcap_better.tsv"
        elif "bike_id" in fields:
            mock_file = "mock_redcap_bikeatrain.tsv"
        elif "ambi_id" in fields:
            mock_file = "mock_redcap_ambi.tsv"
        elif "pacr_id" in fields:
            mock_file = "mock_redcap_pacr.tsv"
        elif "alertid" in fields:
            mock_file = "mock_redcap_alert.tsv"
        elif "normative_id" in fields:
            mock_file = "mock_redcap_normative.tsv"
        else:
            raise ValueError("project not found!")

        df = pd.read_csv(os.path.join(test_path,
                                      "data",
                                      "mock_redcap",
                                      mock_file),
                         sep="\t", index_col="lab_id")
        return df


@pytest.mark.parametrize("lab_id,project,expected_participant_id",
                         [
                             (45, "ALERT", "21"),
                             (157, "PACR", "controlSE051"),
                             (472, "Normative", "3795"),
                             (512, "Bike_Pre", "SEA142"),
                             (176, "AMBI", "21"),
                             (517, "Bike_Post", "SEP202"),
                             (78, "BETTER", "GE120014"),
                             (827, "EXTEND", "2103"),
                         ])
def test_redcap_query(lab_id, project, expected_participant_id, monkeypatch):
    monkeypatch.setattr(redcap, "Project", MockProject)

    participant_id = redcap_query(lab_id, project, "fake_api_key")

    assert participant_id == expected_participant_id
