from Engine.GUIElement import Element

class Label(Element):
    """[GUI] Текст"""
    def __init__(self, screen, style, x=0, y=0, text="", maxLength=40, enable=True, visible=True):
        """Коснтруктор\nПринимает: (Window) screen - окно в котором необходимо рисовать, (Style) style - стиль, (int) x - коорината x, (int) y - координата y, (string) text - текст, (int) maxLength - максимальная длинна текста в символах, (bool) enable - состояние, (bool) visible - отрисовывать ли элемент"""
        super().__init__(screen, style, x, y, text, enable, visible)
        self.maxLength = maxLength
    
    def draw(self):
        """Отрисовка"""
        if self.visible:
            self.screen.text(self.x, self.y, self.text[:self.maxLength], text_prefix=self.style["background"] + self.style["text"])