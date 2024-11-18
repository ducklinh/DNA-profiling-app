# DNA profiling app

## API
Ik heb geen ervaring met het opzetten van een API in Python. Daarom heb ik 
de beschrijving gevolgd en gekozen voor FastAPI.

Ik heb een GET-method gebouwd, omdat informatie wordt opgehaald. In een 
ideale situatie zou ik een GET combineren met een requestbody, omdat 
browsers en HTTP-servers vaak een limiet hebben op URL-lengtes, wat 
problematisch kan zijn voor lange sequenties. Daarnaast bij extra parameters 
kan dezelfde endpoint gebruikt worden, waarbij alleen de request body wordt 
uitgebreid. Helaas is het combineren van een GET met een request body niet 
mogelijk. Als deze beperkingen relevant zouden zijn dan had ik gekozen voor een 
POST-methode,ondanks dat een POST in principe niet bedoeld is om informatie 
op te halen.

De implementatie staat in `api.py`. De functie `check_for_match` valideert 
eerst de ingevoerde parameters. Daarna roept deze de functie 
`profiel_past_in_spoor` aan, die controleert of de sequenties overeenkomen. Tot 
slot maakt de API een response op basis van de bevindingen. 

De functie `check_for_match` maakt gebruik van een `try-except` om onder 
andere een `ValueError` op te vangen wanneer de input incorrect is. In dat 
geval stuurt de API een response met statuscode 400 terug om aan te geven 
dat de fout bij de client ligt. De foutmelding wordt meegegeven, waarbij ik 
deze code toepas: `message = str(e).split("\n")`. Dit voorkomt dat een `\n` 
in de foutmelding letterlijk wordt weergegeven in JSON. Ik wilde de code in 
`domains.py` niet aanpassen, dus heb ik de foutmelding als lijst verwerkt.
Naast `ValueError` worden onverwachte fouten opgevangen, gelogd en met 
statuscode 500 als response teruggestuurd.

## Testen en Pipeline
Ik heb enkele unit- en integratietests geschreven, en een aparte benchmarktest
toegevoegd om de API-prestaties te meten. De benchmark draait meerdere keren
per input en produceert een tijdsrapport.

Het configureren van een CI/CD-pipeline in GitHub was nieuw voor mij. 
Gelukkig biedt GitHub een template voor Python-applicaties. Deze bevatte al 
een codekwaliteit-check (flake8) en een teststap. Ik heb de tests 
opgesplitst in drie stappen: unit, integratie en benchmark. Bij een fout is 
zo sneller te zien welke testen falen.

## Docker
Ik heb een `Dockerfile` en `compose.yaml` gemaakt om de applicatie in Docker te 
draaien. Hoewel mijn kennis van `Docker` beperkt is, denk ik dat deze 
bestanden het minimale bevatten dat nodig is om de applicatie correct te 
laten werken