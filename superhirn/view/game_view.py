class GameView:

    def print_game_board(self, questions: list, ratings: list, role: str, code: str):
        """
        Prints the current game-board.
        """
        questions.reverse()
        ratings.reverse()
        output = zip(questions, ratings)
        print("Spielfeld")
        print("--------------------------------------------------")
        if role == "Codierer":
            print("Code: " + code)
        else:
            print("Code: XXXXX")
        print("")
        for item1, item2 in output:
            print(item1, "|", item2)
        print("--------------------------------------------------")
