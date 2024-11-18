import pytest
from api import check_for_match, _valideer_request, _maakResponse
from domains import DNASpoor, DNAProfiel


def _mock_profiel_past_in_spoor(dna_spoor, dna_profiel):
    return True if dna_spoor == dna_profiel else False


@pytest.mark.parametrize(
    "spoor, profiel, match, expected_response",
    [
        ("ACTG", "ACTG", True,
         "Het DNA profiel past in spoor: ACTG vs ACTG"),
        ("ACTG", "ACTCGA", False,
         "Het DNA profiel past niet in spoor: ACTG vs ACTCGA")
    ]
)
def test_check_for_match(spoor: str, profiel: str, match: bool,
                         expected_response: str, mocker):
    mocker.patch("api.profiel_past_in_spoor", return_value=match)

    response = check_for_match(spoor, profiel)

    assert response == expected_response


def test_valideer_request():
    spoor = "ACTG"
    profiel = "ACTG"
    dna_spoor, dna_profiel = _valideer_request(spoor, profiel)

    assert isinstance(dna_spoor, DNASpoor)
    assert isinstance(dna_profiel, DNAProfiel)
    assert dna_spoor.sequentie == spoor
    assert dna_profiel.sequentie == profiel


@pytest.mark.parametrize(
    "spoor, profiel, expected_match, expected_response",
    [
        ("ACTG", "ACTG", True, "Het DNA profiel past in spoor: "
                               "ACTG vs ACTG"),
        ("ACTG", "AAAA", False, "Het DNA profiel past niet in "
                                "spoor: ACTG vs AAAA")
    ]
)
def test_maak_response(spoor: str, profiel: str, expected_match: bool,
                       expected_response: str):
    response = _maakResponse(spoor, profiel, expected_match)
    assert response == expected_response
