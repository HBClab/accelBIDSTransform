import os
import pandas as pd


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