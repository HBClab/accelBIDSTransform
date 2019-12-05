import os
import pandas as pd
import redcap

from ..redcap_query import redcap_query


class MockProject:

    def __init__(self, url, key):
        pass

    @staticmethod
    def export_records(fields, records=None, format='df'):
        test_path = os.path.dirname(os.path.realpath(__file__))
        df = pd.read_csv(os.path.join(test_path, "data", "mock_redcap_response.tsv"),
                         sep="\t", index_col="lab_id")
        return df


def test_redcap_query(monkeypatch):
    monkeypatch.setattr(redcap, "Project", MockProject)

    participant_id = redcap_query(827, "EXTEND", "B95B2DAAE1ADE9DC8D5F8BF6B7BC97E2")

    assert participant_id == '2103'
