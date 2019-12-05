import os

from .. import utils
from ..bids_transform import bids_transform


def test_bids_transform(monkeypatch):
    def mock_bids(path):
        test_dir = os.path.dirname(os.path.realpath(__file__))
        fake_server = os.path.join(
            test_dir,
            "data",
            "vosslabhpc",
            "Projects",
            "BikeExtend",
            "3-Experiment",
            "2-Data",
            "BIDS")

        return fake_server

    monkeypatch.setattr(utils, "get_test_data_path", mock_bids)

    bids_transform("BikeExtend", 2103, 3)
