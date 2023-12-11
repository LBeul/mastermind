class GameView:
    def print_game_board(self, questions: list, ratings: list):
        """
        Prints the current game-board.
        """
        questions.reverse()
        ratings.reverse()
        output = zip(questions, ratings)
        for item1, item2 in output:
            print(item1,"|",item2)
