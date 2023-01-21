from Engine.Element import Element

class Label(Element):
    """[GUI] Текст"""
    def __init__(self, screen, style, x=0, y=0, text="", maxLength=40, enable=True, visible=True):
        """[GUI] Текст"""
        super().__init__(screen, style, x, y, text, enable, visible)
        self.maxLength = maxLength
    
    def draw(self):
        """Отрисовка"""
        if self.visible:
            self.screen.text(self.text[:self.maxLength], self.x, self.y, wordPrefix=self.style["background"] + self.style["text"])