class GameView:
    def print_game_board(questions: list, ratings: list):
        """
        Prints the current game-board.
        """
        questions.reverse()
        ratings.reverse()
        output = zip(questions, ratings)
        print("Spielfeld")
        print("--------------------------------------------------")
        for item1, item2 in output:
            print(item1, "|", item2)
        print("--------------------------------------------------")
