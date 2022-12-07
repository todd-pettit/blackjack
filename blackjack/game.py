import deck, hand, card

class Game:

    def __init__(self, deck, player_hand, dealer_hand):
        self.deck = deck
        self.player_hand = player_hand
        self.dealer_hand = dealer_hand
