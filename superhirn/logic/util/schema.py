superhirn_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://htwberlin.com/ssr/superhirnserver/move_schema.json",
    "title": "Move",
    "_comment": "Farbkodierung= 1=Rot, 2=Grün, 3=Gelb, 4=Blau, 5=Orange, 6=Braun, 7=Weiss (Bewertung bzw. "
                "Spielfarbe), 8=Schwarz (Bewertung bzw. Spielfarbe)",
    "gameid": {
        "description": "The Id of a certain game. 0 if you want to start a new game.",
        "type": "integer"
    },
    "gamerid": {
        "description": "The Id (String) of of the gamer. Freely selectable at the beginning of the game.",
        "type": "string"
    },
    "positions": {
        "description": "How many positions (>=1, <=9) does the pattern to be guessed have?. Selectable at the "
                       "beginning of the game.",
        "type": "integer"
    },
    "colors": {
        "description": "What is the maximum number of different colors (>=1, <=8) in the pattern to be guessed?. "
                       "Selectable at the beginning of the game.",
        "type": "integer"
    },
    "value": {
        "description": "Either the attempt to be evaluated (request to the server) or the evaluation (response from "
                       "the server). Empty String at game start.",
        "type": "string"
    },
    "required": [
        "gameid",
        "gamerid",
        "positions",
        "colors",
        "value"
    ]
}
