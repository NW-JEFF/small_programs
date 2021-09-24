import os

class Settings:
    def __init__(self):
        self.width=950
        self.height=790
        self.edge_gap=100
        self.gap=14
        self.span=(self.height-self.gap*5-self.edge_gap*2)//4

        self.game_folder=os.path.dirname(__file__)
        self.font_folder=os.path.join(self.game_folder, 'Fonts')
