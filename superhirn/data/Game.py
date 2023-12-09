class Game:
    def __init__(self, game, questions, ratings):
        self.instance = game
        self.code = None
        self.code_length = None
        self.color_availabilities = None
        self.questions = questions
        self.ratings = ratings

    def set_game(self, game):
        self.game = game

    def set_code(self, code):
        self.code = code

    def set_code_length(self, code_length):
        self.code_length = code_length

    def set_color_availabilities(self, color_availabilities):
        self.color_availabilities = color_availabilities

    def set_questions(self, questions):
        self.questions = questions

    def set_ratings(self, ratings):
        self.ratings = ratings
