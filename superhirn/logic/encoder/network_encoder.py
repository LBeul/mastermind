from typing import Union

import jsonschema as js
import requests

from superhirn.logic.connector.data_controller_interface import DataControllerInterface
from superhirn.logic.encoder.encoder_interface import EncoderInterface
from superhirn.logic.util.code import Code
from superhirn.logic.util.color import Color
from superhirn.logic.util.rating import Rating
from superhirn.logic.util.schema import superhirn_schema


class NetworkEncoder(EncoderInterface):

    def __init__(self, game_data: DataControllerInterface, host: str,
                 gamer_id: str):
        self._game_data = game_data
        self._host = host
        self._game_id = 0
        self._gamer_id = gamer_id
        self._schema = superhirn_schema

    @property
    def game_data(self):
        return self._game_data

    def generate_code(self) -> Code:
        initial_payload = self.construct_payload("")
        try:
            response = self.request_colors(initial_payload, True)
            return Code(response)
        except:
            raise Exception("Code couldn't be generated.")

    def rate(self, code_guess) -> Rating:
        """
        Requests a rating from the server and constructs a Rating instance from its response
        :param code_guess: the guess made by the decoder
        :return: the rating calculated by the server
        """
        payload = self.construct_payload(code_guess.to_int_string())
        response = self.request_colors(payload)
        return Rating(response)

    def request_colors(self, payload, is_first: bool = False) -> list[Color]:
        """
        Requests a code/rating from the server via HTTP Post Request.
        If it's the first request of the game, the returned GameID is set for the local session.
        :param payload: the information needed by the server to create a code
        :param is_first: boolean flag that signals if this is the initial request or a follow-up
        :return: the colors that were included in the server response
        """
        headers = {"Content-Type": "application/json"}
        raw_response = requests.post(f"http://{self._host}", json=payload, headers=headers)
        try:
            json_response = raw_response.json()
            try:
                js.validate(instance=json_response, schema=self._schema)
            except (js.exceptions.ValidationError, js.exceptions.SchemaError):
                raise TypeError("The received JSON response is malformed.")
            if is_first:
                self._game_id = json_response["gameid"]
            response_colors = self.str_to_color_list(json_response["value"])
            return response_colors
        except requests.exceptions.JSONDecodeError:
            raise TypeError("API did not return valid JSON.")

    def construct_payload(self, value: str) -> dict[str, Union[int, str]]:
        """
        Wraps a given code string into the specification given in the JSON schema.rater
        Performs a schema validation before returning it
        :param value: the code as a string of numbers
        :return: a dictionary that matches the JSON schema and contains the code
        """
        payload = {
            "gameid": self._game_id,
            "gamerid": self._gamer_id,
            "positions": self._game_data.get_code_length(),
            "colors": self._game_data.get_number_of_colors(),
            "value": value
        }
        try:
            js.validate(instance=payload, schema=self._schema)
            return payload
        except (js.exceptions.ValidationError, js.exceptions.SchemaError):
            raise TypeError("The created payload does not satisfy the schema")

    def str_to_color_list(self, code_str) -> list[Color]:
        """
        Transforms a string into a Color list instance
        :param code_str: The rating received from the server
        :return: a list containing the color values for each given integer in the string
        """
        colors: list[Color] = []
        for char in code_str:
            colors.append(Color(int(char)))
        return colors
