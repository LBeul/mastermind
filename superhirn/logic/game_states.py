from enum import Enum


class GameStates(Enum):
    SETUP = 0
    START = 1
    ENTER_CODE = 2
    DECODER_TURN = 3
    ENCODER_TURN = 4
    CODE_CRACKED = 5
    NO_MORE_TURNS = 6
