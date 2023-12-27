from superhirn.data.code import Code
from superhirn.data.data_interface import DataInterface
from superhirn.data.rating import Rating


class Game(DataInterface):
    code = None
    code_length = None
    color_availabilities = None
    questions = []
    ratings = []

    def set_code(self, given_code: Code):
        self.code = given_code

    def get_code(self) -> Code:
        return self.code

    def set_code_length(self, given_code_length: int):
        self.code_length = given_code_length

    def get_code_length(self) -> int:
        return self.code_length

    def set_color_availabilities(self, given_color_availabilities):
        self.color_availabilities = given_color_availabilities

    def get_color_availabilities(self) -> int:
        return self.color_availabilities

    def add_question(self, given_question: Code):
        self.questions.append(given_question)

    def add_rating(self, given_rating: Rating):
        self.ratings.append(given_rating)
