class Frame:
    """[GUI] Основа кадра и заливка фона"""
    
    def __init__(self, screen, style):
        """[GUI] База кадра и фона\nПринимает: (Window) screen - окно для отрисовки, (Style) style - стиль"""
        self.screen = screen
        self.style = style
    
    def draw(self):
        """Отрисовка"""
        self.screen.fill(self.style["background"] + " ")