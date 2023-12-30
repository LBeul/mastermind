from superhirn.logic.util.color import Color


def color_string_to_list(color_string: str) -> list[Color]:
    return [Color(int(val)) for val in color_string]
