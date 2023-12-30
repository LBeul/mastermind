from superhirn.logic.util.color import Color


class Code:

    def __init__(self, colors: list[Color]):
        self._colors = colors

    def get_color_at(self, number: int) -> Color:
        """
        Return color at given index.
        :param number: Index of color in array
        :return: Color object
        """
        return self._colors[number]

    def to_int_list(self):
        """
        Return code in list format containing the int values of the color enum
        :return: List containing the color values
        """
        return [c.value for c in self._colors]

    def to_int_string(self) -> str:
        """
        Returns the current code as a string.
        :return: Code as string.
        """
        int_list = self.to_int_list()
        return ''.join(str(i) for i in int_list)

    def get_length(self) -> int:
        """
        Returns length of current code.
        :return: code length as an integer.
        """
        return len(self._colors)

    def __str__(self):
        """
        Return string-formatted list of colors within the Code
        :return: string containing the colors of the code
        """
        return self.to_int_list().__str__()

    def get_colors(self) -> list[Color]:
        """
        Returns the list of colors.
        :return: List of colors.
        """
        return self._colors
