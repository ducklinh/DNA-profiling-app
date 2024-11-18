from main import profiel_past_in_spoor
from domains import DNASpoor, DNAProfiel


def test_profiel_past_in_spoor():
    spoor = DNASpoor("ACTG")
    profiel = DNAProfiel("ACTG")
    assert (profiel_past_in_spoor(spoor, profiel))


def test_profiel_past_niet_in_spoor():
    spoor = DNASpoor("ACTG")
    profiel = DNAProfiel("AAAA")
    assert not (profiel_past_in_spoor(spoor, profiel))


def test_langere_profiel_past_niet_in_spoor():
    spoor = DNASpoor("ACTG")
    profiel = DNAProfiel("ACTGAAAA")
    assert not (profiel_past_in_spoor(spoor, profiel))
