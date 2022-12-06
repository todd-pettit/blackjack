import card
import random

class Deck:
    def __init__(self):
        suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
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

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def cut_deck(self):
        deck_length = len(self.deck)
        cut_selection = round(deck_length/2)
        partition1 = self.deck[:cut_selection]
        partition2 = self.deck[cut_selection:]
        self.deck = [partition2 + partition1]


if __name__ == '__main__':
    current_deck = Deck()
    current_deck.show_deck()
    current_deck.shuffle_deck()
    current_deck.show_deck()
    current_deck.cut_deck()
    current_deck.show_deck()
