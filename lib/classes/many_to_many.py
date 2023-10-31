class Game:

    all = []

    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        if isinstance(title,str) and len(title):
            self._title = title

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        results = [result.score for result in self.results()]
        return sum(results) / len(results)

class Player:

    all = []

    def __init__(self, username):
        self.username = username
        type(self).all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self,username):
        if isinstance(username,str) and len(username) >1 and len(username) < 17:
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        for my_game in self.games_played():
            if(my_game.title == game.title):
                return True
        return False

    def num_times_played(self, game):
        return [result.game for result in Result.all if result.player == self].count(game)

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,score):
        if not hasattr(self,"score"):
            self._score = score