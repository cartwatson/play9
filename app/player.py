from collections import Counter
from card import Card


class Player:
    def __init__(self):
        # cards are in two arrays, same index indicates alignment
        self.__hand: list[list[Card]] = [[], []]
        self.__score: int = 0

    def add_to_score(self, round_score: int) -> None:
        self.__score += round_score

    def get_score(self) -> int:
        return self.__score

    def hand_to_str(self) -> str:
        hand_string = ""
        for i in range(2):
            hand_string += "/----\\" * 4 + "\n" + "|    |" * 4 + "\n"
            for j in range(4):
                if self.__hand[i][j].is_face_up():
                    hand_string += "| {:02d} |".format(self.__hand[i][j].get_value())
                else:
                    hand_string += "| -- |"
            hand_string += "\n" + "|    |" * 4 + "\n" + "\\----/" * 4 + "\n"
        return hand_string

    def print_hand(self) -> None:
        print(self.hand_to_str())

    def clear_hand(self) -> None:
        self.__hand = [[], []]

    def fill_hand(self, card: Card) -> None:
        if len(self.__hand[0]) < 4:
            self.__hand[0].append(card)
        elif len(self.__hand[1]) < 4:
            self.__hand[1].append(card)
        else:
            raise Exception("player was dealt too many cards!")

    def score_hand(self) -> int:
        score = 0
        cancelled_cards: Counter = Counter()  # used for when you get multiple cancellations of the same card
        for i in range(2):
            for j in range(4):
                # do not let player score their card if they can't see it
                if not self.__hand[i][j].is_face_up():
                    continue

                # check for cancellation
                if (
                    self.__hand[0][j].get_value() == self.__hand[1][j].get_value()
                    # don't cancel out if you can't see the other vertical card
                    and self.__hand[0][j].is_face_up()
                    and self.__hand[1][j].is_face_up()
                ):
                    cancelled_cards.update([self.__hand[0][j].get_value()])
                    score += -5 if self.__hand[0][j].get_value() == -5 else 0
                else:  # card doesn't match above/below card
                    score += self.__hand[i][j].get_value()

        # logic for more than one set of cancelled cards
        for cards in cancelled_cards.most_common(None):
            score_adjustments = {
                4: -10,
                6: -15,
                8: -20
            }
            score += score_adjustments.get(cards[1], 0)
        return score

    def flip_out(self) -> None:
        for i in range(2):
            for j in range(4):
                self.__hand[i][j].set_face_up()

    def face_up_cards(self) -> list[int]:
        face_up = []
        for i in range(2):
            for j in range(4):
                if self.__hand[i][j].is_face_up():
                    face_up.append(self.__hand[i][j].get_value())
        return face_up

    def is_flipped_out(self) -> bool:
        return len(self.face_up_cards()) == 8

    # AI: SECTION
    def tee_off(self) -> None:
        # TODO AI: let player decide which cards to flip
        pass

    def chose_draw_from_deck(self, face_up_cards: list[int], discard_value: int) -> bool:
        # TODO AI: did the player choose to draw or take the top card from discard
        return True  # BUG

    # TODO: can maybe combine the below with a bool arg for deck/discard
    def turn_draw_from_deck(self, card) -> Card:
        # TODO AI:
        # replace existing card and discard replaced card
        # OR
        # discard drawn card and flip facedown card
        return Card(-1)  # BUG

    def turn_draw_from_discard(self, card) -> Card:
        # TODO AI:
        # replace existing card and discard replaced card
        return Card(-1)  # BUG
