
# Exercise: In contract bridge, a "trick" is a round of play in which each of four players plays one card.
# To represent those cards, we'll define a class that inherits from Deck.
# As an example, consider this trick, where the first player leads with the 3 of Diamonds,
# which means that Diamonds are the "led suit".
# The second and third players "follow suit", which means they play a card with the led suit.
# The fourth player plays a card of a different suit, which means they cannot win the trick.
# So the winner of this trick is the third player, because they played the highest card in the led suit.
# Write a Trick method called find_winner that loops through the cards in the Trick and returns the index of the card that wins.
# In the previous example, the index of the winning card is 2.
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self, cards):
        self.cards = cards

class Trick(Deck):
    def find_winner(self, trump_suit):
        winning_card_index = 0
        winning_card_rank = self.cards[0].rank
        winning_card_suit = self.cards[0].suit

        for i in range(1, len(self.cards)):
            card = self.cards[i]
            if card.suit == trump_suit:
                if card.rank > winning_card_rank:
                    winning_card_index = i
                    winning_card_rank = card.rank
                    winning_card_suit = card.suit
            elif card.suit == winning_card_suit:
                if card.rank > winning_card_rank:
                    winning_card_index = i
                    winning_card_rank = card.rank

        return winning_card_index
    
cards = [Card(1, 3),
         Card(1, 10),
         Card(1, 12),
         Card(2, 13)]
trick = Trick(cards)
print(trick.find_winner(cards))