import random
class Player:
    """An AI player for Connect Four."""
    from board import Board

    def __init__(self, ox, tbt, ply):
        """Construct a player for a given checker, tie-breaking type,
           and ply."""
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__(self) -> str:
        """Create a string represenation of the player."""
        s = "Player: ox = " + self.ox + ", "
        s += "tbt = " + self.tbt + ", "
        s += "ply = " + str(self.ply)
        return s
    
    def opp_ch(self) -> str:
        """Gets the opponent char the player is playing against."""
        if self.ox != 'O': return 'O'
        return 'X'
    
    def score_board(self, b: Board) -> float:
        if b.wins_for(self.ox): return 100.0
        elif b.wins_for(self.opp_ch()): return 0.0
        else: return 50.0
        
    def tiebreak_move(self, scores: list[float]) -> int:
        # Voor snelheid is er gekozen voor drie verschillende for loops,
        # dit kan allemaal in 1 loop als snelheid niet uitmaakt.

        # (Index, Amount)
        highest = (None, -1)

        # Left calcs
        if self.tbt == "LEFT":
            for idx, score in enumerate(scores):
                if score > highest[1]:
                    highest = (idx, score)
            return highest[0]
        # Right calcs
        if self.tbt == "RIGHT":
            for idx, score in enumerate(scores):
                if score >= highest[1]:
                    highest = (idx, score)
            return highest[0]
        # Random calcs
        if self.tbt == "RANDOM":
            l = []
            for idx, score in enumerate(scores):
                if score > highest[1]:
                    highest = (idx, score)
            for idx, score in enumerate(scores):
                if score == highest[1]:
                    l.append(idx)
            return l[random.randrange(len(l) -1)]
            
    def scores_for(self, b: Board) -> list:
        scores = [50.0] * b.width

        if not b.allows_move(scores[0]):
            scores[0] = -1.0
            return scores
        elif b.wins_for(self.ox):
            scores[0] = 100.0
            return scores
        elif b.wins_for(self.opp_ch()):
            scores[0] = 0.0
            return scores
        elif self.ply <= 0:
            scores[0] = 50.0
            return scores


        return scores