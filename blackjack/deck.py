import card

class Deck:
    def __init__(self):
        suits = ["clubs", "hearts", "diamonds", "spades"]
        values = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
        deck = []
        for suit in suits:
            for value in values:
                current_card = card.Card(suit, value)
                deck.append(current_card)
                self.deck = deck

    def show_deck(self):
        for card in self.deck:
            print(card.value, "of", card.suit)

if __name__ == '__main__':
    current_deck = Deck()
    current_deck.show_deck()
