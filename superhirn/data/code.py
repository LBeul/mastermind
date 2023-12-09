from superhirn.data import color


class Code:

    def __init__(self, colors: list[color]):
        self.colors = colors

    def get_color_at(self, number: int) -> color:
        """
        Return color at given index.
        :param number: Index of color in array
        :return: Color object
        """
        return self.colors[number]
