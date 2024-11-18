import pytest
from fastapi.testclient import TestClient
from api import app


client = TestClient(app)


@pytest.mark.parametrize(
    "spoor, profiel, expected_response",
    [
        ("ACTG", "ACTG", '"Het DNA profiel past in spoor: ACTG vs ACTG"'),
        ("ACTG", "AAAA", '"Het DNA profiel past niet in spoor: ACTG vs AAAA"')
    ]
)
def test_profiel_komt_overeen_met_spoor(spoor: str, profiel: str,
                                        expected_response: str):
    response = _post_request(spoor, profiel)

    assert response.status_code == 200
    assert response.text == expected_response


@pytest.mark.parametrize(
    "spoor, profiel, expected_response",
    [
        ("Ongeldig", "ACTG", {"detail": ["Een DNASpoor mag alleen bestaan "
                                         "uit:ATCGWSMKRYBDHVN",
                                         "Opgeven sequentie: Ongeldig"]}),
        ("ACTG", "Ongeldig", {"detail": ["Een DNAProfiel mag alleen bestaan "
                                         "uit:ATCG",
                                         "Opgeven sequentie: Ongeldig"]})
    ]
)
def test_ongeldige_request(spoor: str, profiel: str, expected_response: str):
    response = _post_request(spoor, profiel)

    assert response.status_code == 400
    assert response.json() == expected_response


def _post_request(spoor: str, profiel: str):
    response = client.get(
        f"/check-for-match/{spoor}/{profiel}"
    )
    return response
