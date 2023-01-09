from Core.Mmath import Mmath

class Grid:
    """Визуальный разделитель окна в соответсвии с кол-вом столбцов и строк"""

    def __init__(self, screen, x, y, w, h, columns, strings, style):
        self.screen = screen
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.columns = columns
        self.strings = strings
        self.style = style

        self.cellW = Mmath.round((w - (columns - 1)) / columns)
        self.cellH = Mmath.round((h - (strings - 1)) / strings)
    
    def intersection(self, x, y):
        x1 = x // self.cellW
        y1 = y // self.cellH
        return (x1, y1)
    
    def draw(self):
        for i in range(1, self.columns):
            self.screen.line(self.x + i * self.cellW, self.y, self.x + i * self.cellW, self.y + self.h, self.style["background"] + self.style["text"] + "|")
        
        for i in range(1, self.strings):
            self.screen.line(self.x, self.y + i * self.cellH, self.x + self.w, self.y + i * self.cellH, self.style["background"] + self.style["text"] + "-")