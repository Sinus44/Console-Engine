class Grid:
    """[GUI] Визуальная сетка"""

    def __init__(self, window:object, x:int, y:int, w:int, h:int, columns:int, strings:int, style:object):
        self.window = window
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.columns = columns
        self.strings = strings
        self.style = style

        self.cellW = (w - (columns - 1)) // columns
        self.cellH = (h - (strings - 1)) // strings
    
    def intersection(self, x:int, y:int):
        """Вовзращает координаты в сетке"""
        x1 = x // self.cellW
        y1 = y // self.cellH
        return (x1, y1)
    
    def draw(self):
        """Отрисовка"""
        for i in range(1, self.columns):
            self.window.line(self.x + i * self.cellW, self.y, self.x + i * self.cellW, self.y + self.h, self.style.background + self.style.text + "|")
        
        for i in range(1, self.strings):
            self.window.line(self.x, self.y + i * self.cellH, self.x + self.w, self.y + i * self.cellH, self.style.background + self.style.text + "-")