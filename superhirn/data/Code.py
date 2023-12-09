from superhirn.data.Color import Color

class Code:

    def __init__(self, colors):
        self.colors = colors

    def get_color_at(self, number):
        return self.colors[number]
