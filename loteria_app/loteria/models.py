from loteria_app import db
from random import shuffle


class Loteria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qtd_dozens = db.Column(db.Integer)
    result = db.Column(db.String(200))
    total_games = db.Column(db.Integer)
    games = db.Column(db.String(200))

    def __init__(self, qtd_dozens, total_games):
        if qtd_dozens not in [6, 7, 8, 9, 10]:
            raise Exception("É permitido somente as dezenas 6, 7, 8, 9, 10")
        self.qtd_dozens = qtd_dozens
        self.total_games = total_games

    def _get_dozens_array(self):
        qtd_dozens = self.qtd_dozens
        random = [i for i in range(1, 61)]
        shuffle(random)
        dozens_list = []
        for i in random:
            if len(dozens_list) == qtd_dozens:
                break
            if i not in dozens_list:
                dozens_list.append(i)
        dozens_list.sort()
        return dozens_list

    def generate_games(self):
        total_games = self.total_games
        games = {}
        for i in range(1, (total_games + 1)):
            generate_game = self._get_dozens_array()
            games.update({i: generate_game})

        self.games = games

    def generate_lottery(self):
        random = [i for i in range(1, 61)]
        shuffle(random)
        random_lottery = []
        for i in random:
            if len(random_lottery) == 6:
                break
            count += 1
            random_lottery.append(i)
        random_lottery.sort()
        self.result = random_lottery

