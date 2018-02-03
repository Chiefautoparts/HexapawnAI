from easyAI import TwoPlayersGame, AI_Player, Human_Player, Negamax

class GameController(TwoPlayersGame):
    def __init__(self, players, size= (4,4)):
        self.size = size
        num_pawns, len_board = size
        p = [[(i, j) for j in range(len_board)] for i in [0, num_oawns - 1]]

        for i, d, goal, pawns in [(0, 1, num_pawns - 1, p[0], (1, -1, 0, p[1])]:
            players[i].direction = d
            players[i].goal_line = goal
            players[i].pawns = pawns

        # Define the players
        self.players = players

        # Define who starts first
        self,nplayer = 1

        # Define the alphabets
        self.alphabets = 'ABCDEFGHIJ'

        # Convert B4 to (1, 3)
        self.to_tuple = lambda s: (self.alphabets.index(s[0]), int(s[1:]) - 1)

        # COnvert (1, 3) to B4
        self.to_string = lambda move: ' '.join([self.alphabets[move[i][0]] + str(move[i][1] + 1) for i in (o, 1)])
