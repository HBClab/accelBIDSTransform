import pytest

from ..bids_transform import bids_transform


@pytest.mark.parametrize(
    "project,sub_id,ses_id,expected_path",
    [
        ("ALERT", "21", None,
         ('vosslabhpc/Projects/ALERT/3-Experiment/2-Data/BIDS/'
          'sub-21/beh/sub-21_accel.csv')),
        ("PACR", "51", "pre",
         ('vosslabhpc/Projects/PACR-AD/Imaging/BIDS/'
          'sub-controlSE051/ses-pre/beh/sub-controlSE051_ses-pre_accel.csv')),
        ("Normative", "3795", None,
         ('vosslabhpc/Projects/NormativeSample/3-Experiment/2-Data/BIDS/'
          'sub-3795/beh/sub-3795_accel.csv')),
        ("BIKE_Pre", "142", "pre",
         ('vosslabhpc/Projects/Bike_ATrain/Imaging/BIDS/'
          'sub-SEA142/ses-pre/beh/sub-SEA142_ses-pre_accel.csv')),
        ("AMBI", "21", None,
         ('vosslabhpc/Projects/AMBI/3-Experiment/2-Data/Imaging/BIDS/'
          'sub-21/beh/sub-21_accel.csv')),
        ("BIKE_Post", "202", "post",
         ('vosslabhpc/Projects/Bike_ATrain/Imaging/BIDS/'
          'sub-SEP202/ses-post/beh/sub-SEP202_ses-post_accel.csv')),
        ("BETTER", "120014",  "pre",
         ('vosslabhpc/Projects/BETTER/3-Experiment/2-data/bids/'
          'sub-GE120014/ses-pre/beh/sub-GE120014_ses-pre_accel.csv')),
        ("EXTEND", "2103", "3",
         ('vosslabhpc/Projects/BikeExtend/3-Experiment/2-Data/BIDS/'
          'sub-2103/ses-accel3/beh/sub-2103_ses-accel3_accel.csv'))
    ])
def test_bids_transform(project, sub_id, ses_id, expected_path):

    path = bids_transform(project, sub_id, ses_id)

    assert path == expected_path
