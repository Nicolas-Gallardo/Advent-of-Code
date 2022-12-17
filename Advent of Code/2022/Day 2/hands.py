class Player:

    def __init__(self):
        self.score = 0
        self.hand = None
    
    def set_hand(self, hand):
        self.hand = hand(self)

    def play_against(self,player):
        self.hand.play_against(player.hand)
        player.hand.play_against(self.hand)
        self.score += self.hand.hand_score

    def draw_hand(self, hand):
        self.set_hand(type(hand))

    def lose_hand(self, hand):
        if type(hand) == Paper:
            self.set_hand(Rock)
        elif type(hand) == Rock:
            self.set_hand(Scissor)
        elif type(hand) == Scissor:
            self.set_hand(Paper)

    def win_hand(self, hand):
        if type(hand) == Paper:
            self.set_hand(Scissor)
        elif type(hand) == Rock:
            self.set_hand(Paper)
        elif type(hand) == Scissor:
            self.set_hand(Rock)
    
class Paper:

    def __init__(self, player):
        self.player = player
        self.hand_score = 2

    def play_against(self, a_hand):
        if type(a_hand) == Paper:
            self.player.score += 3
        if type(a_hand) == Rock:
            self.player.score += 6
        if type(a_hand) == Scissor:
            self.player.score += 0

class Rock:

    def __init__(self, player):
        self.player = player
        self.hand_score = 1

    def play_against(self, a_hand):
        if type(a_hand) == Paper:
            self.player.score += 0
        if type(a_hand) == Rock:
            self.player.score += 3
        if type(a_hand) == Scissor:
            self.player.score += 6

class Scissor:

    def __init__(self, player):
        self.player = player
        self.hand_score = 3

    def play_against(self, a_hand):
        if type(a_hand) == Paper:
            self.player.score += 6
        if type(a_hand) == Rock:
            self.player.score += 0
        if type(a_hand) == Scissor:
            self.player.score += 3