import pytest
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

matching_cases = [["CCCSMAYVMH", "CCCCAACCAC"], ["CYWGATVDCH", "CCTGATATCT"],
["DTGVDNCT", "TTGAGACT"]]

non_matching_cases = [["VCYDRYTHG", "TGGGG"], ["RNNYT", "ATTC"],
                      ["YBCWKNYTMB", "TAGCGC"]]

@pytest.mark.benchmark
@pytest.mark.parametrize(
    "spoor, profiel, match",
    [
        (*case, True) for case in matching_cases
    ] + [
        (*case, False) for case in non_matching_cases
    ]
)
def test_check_for_match(benchmark, spoor, profiel, match):
    result = benchmark(
        lambda: _post_request(spoor, profiel))

    assert result.status_code == 200

    expected_response = (
        f'"Het DNA profiel past in spoor: {spoor} vs {profiel}"'
        if match else
        f'"Het DNA profiel past niet in spoor: {spoor} vs {profiel}"'
    )

    assert result.text == expected_response



def _post_request(spoor: str, profiel: str):
    response = client.get(
        f"/check-for-match/{spoor}/{profiel}"
    )
    return response

