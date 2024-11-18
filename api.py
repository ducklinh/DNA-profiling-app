from fastapi import FastAPI, HTTPException
from starlette.responses import PlainTextResponse

from main import profiel_past_in_spoor
from domains import DNASpoor, DNAProfiel

import logging


app = FastAPI()


@app.get("/check-for-match/{dna_spoor}/{dna_profiel}")
def check_for_match(dna_spoor: str, dna_profiel: str)-> str:
    try:
        gevalideerde_spoor, gevalideerde_profiel = _valideer_request(dna_spoor,
                                                          dna_profiel)

        match = profiel_past_in_spoor(gevalideerde_spoor, gevalideerde_profiel)

        return _maakResponse(dna_spoor, dna_profiel,
                             match)
    except ValueError as e:
        message = str(e).split("\n")
        raise HTTPException(status_code=400, detail=message)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Unexpected error")


def _valideer_request(dna_spoor: str, dna_profiel: str) -> (DNASpoor,
                                                            DNAProfiel):
    return DNASpoor(dna_spoor), DNAProfiel(dna_profiel)


def _maakResponse(dna_spoor: str, dna_profiel: str, match: bool) -> str:
    if match:
        response = (f"Het DNA profiel past in spoor: {dna_spoor} "
                    f"vs {dna_profiel}")
    else:
        response = (f"Het DNA profiel past niet in spoor: {dna_spoor} "
                    f"vs {dna_profiel}")

    return response
