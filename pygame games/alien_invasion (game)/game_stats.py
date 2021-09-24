
class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings=ai_settings
        self.reset_stats()
        self.game_active=False
        try:
            with open('high_score_record.txt', 'x') as f:
                f.write('0')
        except FileExistsError:
            pass
        self.high_score= int(open('high_score_record.txt').readline())
        self.level=1

    def reset_stats(self):
        self.ships_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1
