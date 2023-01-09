from Core.Element import Element

class Label(Element):
    """GUI - элемент текст"""
    
    def draw(self):
        if self.visible:
            self.screen.text(self.text, self.x, self.y, wordPrefix=self.style["background"] + self.style["text"])