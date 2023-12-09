from superhirn.data.Color import Color


class Rating:

    def __init__(self, colors):
        self.colors = colors

    def count_white(self):
        count_white = self.colors.count(Color.WHITE)
        return count_white

    def count_black(self):
        count_black = self.colors.count(Color.WHITE)
        return count_black
