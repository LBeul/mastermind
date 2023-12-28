from superhirn.data.code import Code
from superhirn.data.rating import Rating
from superhirn.logic.connector.data_controller_interface import DataControllerInterface


class Game(DataControllerInterface):
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

    def set_number_of_colors(self, given_number_of_colors):
        self.color_availabilities = given_number_of_colors

    def get_number_of_colors(self) -> int:
        return self.color_availabilities

    def add_question(self, given_question: Code):
        self.questions.append(given_question)

    def get_questions(self):
        return self.questions

    def add_rating(self, given_rating: Rating):
        self.ratings.append(given_rating)

    def get_ratings(self):
        return self.ratings
