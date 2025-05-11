import random
from card import Card


class Deck:
    def __init__(self):
        self.__discard_pile: list[Card] = []
        self.__cards: list[Card] = self.__create_deck()
        self.shuffle()

    def __create_deck(self) -> list[Card]:
        cards: list[Card] = []
        for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            for j in range(8):
                cards.append(Card(i))
        for i in range(4):
            cards.append(Card(-5))
        return cards

    def deal(self) -> Card:
        return self.__cards.pop()

    def draw(self) -> Card:
        card = self.deal()
        card.set_face_up()
        return card

    def shuffle(self) -> None:
        random.shuffle(self.__cards)

    def draw_from_discard(self) -> Card:
        return self.__discard_pile.pop(0)

    def discard(self, card: Card) -> None:
        self.__discard_pile.insert(0, card)

    def get_discard_values(self) -> list[int]:
        discard_values: list[int] = []
        for card in self.__discard_pile:
            discard_values.append(card.get_value())
        return discard_values

    def get_discard_top_card_value(self) -> int:
        temp: Card = self.__discard_pile.pop(0)
        self.discard(temp)
        return temp.get_value()

    def cards_remaining(self) -> int:
        return len(self.__cards)

    def reshuffle(self) -> None:
        discard_pile = self.__discard_pile.copy()
        for card in discard_pile:
            card.set_face_down()
        self.__cards += discard_pile
        self.__discard_pile = []
        self.shuffle()
