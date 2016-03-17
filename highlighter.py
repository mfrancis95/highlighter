from os.path import splitext
from re import sub

defaultColors = ["\033[31m", "\033[32m", "\033[33m"]

class Highlighter:

    def __init__(self):
        self.colors = defaultColors
        self.styles = {}

    def highlight(self, file):
        styles = self.styles.get(splitext(file)[1][1:], [])
        with open(file) as f:
            for line in highlight(f, styles, self.colors):
                yield line

def colorize(text, color):
    return color + sub("\033\[..m", "", text) + "\033[39m"

def highlight(file, styles, colors = None):
    if not colors:
        colors = defaultColors
    for line in file:
        for style in styles:
            line = sub(style["pattern"], lambda match: colorize(match.group(), colors[style["color"]]), line)
        yield line
