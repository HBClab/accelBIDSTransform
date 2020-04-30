import redcap
import pytest

from ..redcap_query import redcap_query
from .conftest import MockProject


@pytest.mark.parametrize("lab_id,project,expected_participant_id",
                         [
                             (45, "ALERT", "21"),
                             (157, "PACR", "51"),
                             (472, "Normative", "3795"),
                             (512, "BIKE_Pre", "142"),
                             (176, "AMBI", "021"),
                             (517, "BIKE_Post", "202"),
                             (78, "BETTER", "120014"),
                             (827, "EXTEND", "2103")
                         ])
def test_redcap_query(lab_id, project, expected_participant_id, monkeypatch):
    monkeypatch.setattr(redcap, "Project", MockProject)

    participant_id = redcap_query(lab_id, project, "fake_api_key")

    assert participant_id == expected_participant_id
