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
    """A class representing a playing card.

    Attributes:
        suit (str): The suit of the card (e.g., 'Hearts', 'Spades')
        rank (int): The rank of the card (e.g., 2-10, Jack=11, Queen=12, King=13, Ace=14)
    """

    def __init__(self, suit: str, rank: int):
        """Initialize a Card with a suit and rank.

        Args:
            suit (str): The suit of the card
            rank (int): The rank of the card
        """
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        """Return a string representation of the card.

        Returns:
            str: A string in the format 'rank of suit'
        """
        return f"{self.rank} of {self.suit}"


class Deck:
    """A class representing a collection of cards.

    Attributes:
        cards (list[Card]): A list of Card objects
    """

    def __init__(self, cards=None):
        """Initialize a Deck with a list of cards.

        Args:
            cards (list[Card] | None, optional): The list of cards in the deck.
                Defaults to None, in which case an empty list is used.

        Examples:
        >>> deck1 = Deck()  # Creates empty deck
        >>> deck2 = Deck([Card('Hearts', 10), Card('Spades', 11)])  # Creates deck with 2 cards
        """
        self.cards = cards if cards is not None else []


class Trick(Deck):
    """A class representing a trick in a card game, inheriting from Deck.

    A trick is a collection of cards played in a single round where one suit
    may be designated as trump, having higher priority than other suits.
    """

    def find_winner(self, trump_suit: str) -> int:
        """Find the winning card in the trick considering the trump suit.

        The winner is determined by these rules:
        1. If there are trump cards, the highest trump card wins
        2. Otherwise, the highest card of the leading suit wins

        Args:
            trump_suit (str): The designated trump suit for this trick

        Returns:
            int: The index of the winning card in the trick

        Examples:
            >>> cards = [Card('Hearts', 10), Card('Spades', 11), Card('Hearts', 12)]
            >>> trick = Trick(cards)
            >>> # If Hearts is trump, the King of Hearts wins
            >>> trick.find_winner('Hearts')
            2

        Notes:
            - The led suit is the suit of the first card played in the trick
            - If a player does not have a card in the led suit,
            they can play a card of any other suit, but their card typically cannot win the trick unless it is a trump card.
            - The trump suit is a special suit that has higher priority than other suits
            - Trump suits are typically chosen in advance for a hand or determined by the rules of the game.
        """
        if not self.cards:
            raise ValueError("No cards in the trick.")

        # Separate trump cards and led suit cards
        """
            - trump_cards: a list of tuples (index, card) where the index is the position of the card in the trick and the card is the Card object
            - led_suit_cards: a list of tuples (index, card) where the index is the position of the card in the trick and the card is the Card object.
                But contains only the cards of the led suit (the suit of the first card played in the trick)
        """
        trump_cards = [
            (i, card) for i, card in enumerate(self.cards) if card.suit == trump_suit
        ]
        led_suit = self.cards[0].suit  # assume the first card is the led suit
        led_suit_cards = [
            (i, card) for i, card in enumerate(self.cards) if card.suit == led_suit
        ]

        # Determine the winner
        if trump_cards:
            # Highest trump card wins
            """
            - The key lambda x: x[1].rank is used to sort the list of tuples based on the rank of the card.
            - The max function is used to find the tuple with the highest rank, which corresponds to the highest trump card.
            """
            return max(trump_cards, key=lambda x: x[1].rank)[0]
        else:
            # Highest card of the led suit wins
            return max(led_suit_cards, key=lambda x: x[1].rank)[0]


cards = [
    Card("Diamonds", 3),
    Card("Diamonds", 10),
    Card("Diamonds", 12),
    Card("Hearts", 13),
]
trick = Trick(cards)
print(trick.find_winner("Hearts"))  # Output: 3
print(trick.find_winner("Diamonds"))  # Output: 2
