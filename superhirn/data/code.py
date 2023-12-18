from superhirn.data.color import Color


class Code:

    def __init__(self, colors: list[Color]):
        self.colors = colors

    def get_color_at(self, number: int) -> Color:
        """
        Return color at given index.
        :param number: Index of color in array
        :return: Color object
        """
        return self.colors[number]

    def to_int_list(self):
        """
        Return code in list format containing the int values of the color enum
        :return: List containing the color values
        """
        return [c for c in self.colors]

    def __str__(self):
        """
        Return string-formatted list of colors within the Code
        :return: string containing the colors of the code
        """
        return self.to_int_list().__str__()
