from superhirn.logic.util.code import Code
from superhirn.logic.util.color import Color


class Rating(Code):

    def count_whites(self):
        """
        Counts all white markers in the rating
        :return: Amount of white markers
        """
        count_white = self.get_colors().count(Color.WHITE)
        return count_white

    def count_blacks(self):
        """
        Counts all black markers in the rating
        :return: Amount of black markers
        """
        count_black = self.get_colors().count(Color.BLACK)
        return count_black
