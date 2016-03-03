from re import sub

class Highlighter:

    def __init__(self):
        self.colors = ["\033[31m", "\033[32m", "\033[33m"]
        self.patterns = {}

    def colorize(self, match, color):
        return self.colors[color] + sub("\033\[..m", "", match.group()) + "\033[39m"

    def highlight(self, file, fileType):
        for line in file:
            for pattern in self.patterns[fileType]:
                line = sub(pattern["pattern"], lambda match: self.colorize(match, pattern["color"]), line)
            yield line
