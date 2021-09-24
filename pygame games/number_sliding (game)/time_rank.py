from game_functions import draw_text
import re

class Rank():
    def __init__(self, settings, screen):
        self.settings=settings
        self.screen=screen

        try:
            with open('rank.txt', 'x') as f:
                f.write('1000, 1000, 1000')
        except FileExistsError:
            pass

        pattern=re.compile(r'\d+\.?\d*')
        self.rank=re.findall(pattern, open('rank.txt').readline())


    def draw_me(self):
        x=self.settings.height - self.settings.edge_gap / 2 + (self.settings.width - self.settings.height) / 2
        n=0
        for text in self.rank:
            draw_text(self.settings, self.screen, text, (0,0,20), (x, self.settings.height / 2 -20 - (20+1*n)*n), 23+2*n)
            n+=1
        draw_text(self.settings, self.screen, 'Best 3: ', (0, 0, 0), (x-20, self.settings.height / 2 - 17 - (20 + 2 * n) * n),
                  25)