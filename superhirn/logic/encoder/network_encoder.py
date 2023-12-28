import jsonschema as js
import requests

from superhirn.logic.connector.data_controller_interface import DataControllerInterface
from superhirn.logic.encoder.encoder_interface import EncoderInterface
from superhirn.logic.util.code import Code


class NetworkEncoder(EncoderInterface):

    def __init__(self, game_data: DataControllerInterface, host: str,
                 gamer_id: str):
        self._game_data = game_data
        self._host = host
        self._game_id = 0
        self._gamer_id = gamer_id
        self._schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": "https://htwberlin.com/ssr/superhirnserver/move_schema.json",
            "title": "Move",
            "gameid": {"type": "integer"},
            "gamerid": {"type": "string"},
            "positions": {"type": "integer"},
            "colors": {"type": "integer"},
            "value": {"type": "string"},
            "required": ["gameid", "gamerid", "positions", "colors", "value"]
        }

    @property
    def game_data(self):
        return self._game_data

    def generate_code(self):
        initial_payload = self.construct_payload("")
        try:
            code = self.request_code(initial_payload, is_first=True)
            return code
        except:
            raise Exception("Code couldn't be generated.")

    def rate(self, code_guess):
        payload = self.construct_payload(code_guess.to_int_string())
        rating = self.request_code(payload)
        return rating

    def request_code(self, payload, is_first: bool = False) -> Code:
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

            code = Code(json_response["value"])
            return code
        except requests.exceptions.JSONDecodeError:
            raise TypeError("API did not return valid JSON.")

    def construct_payload(self, value: str):
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
