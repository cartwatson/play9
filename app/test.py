from card import Card
from deck import Deck
from player import Player


def player_scoring():
    player = Player()
    cards = [
         Card(5), Card(5), Card(4), Card(4),
         Card(5), Card(5), Card(4), Card(4)
    ]

    for card in cards:
        card.set_face_up()

    cards[6].set_face_down()

    for i in range(8):
        player.fill_hand(cards.pop(0))

    player.print_hand()
    print(player.score_hand())


def deck_reshuffle():
    deck = Deck()
    for _ in range(50):
        deck.discard(deck.draw())

    print(deck.cards_remaining())
    deck.reshuffle()
    print(deck.cards_remaining())


def read_discard():
    deck = Deck()
    print(deck.cards_remaining())
    deck.discard(deck.draw())
    print(deck.cards_remaining())
    print(deck.get_discard_top_card_value())
    print(deck.cards_remaining())


def flip_out():
    def create_players() -> list[Player]:
        num_players = 4  # 2-6 players recommended
        players = []
        for i in range(num_players):
            players.append(Player())
        return players

    def main():
        players = create_players()

        # play nine holes
        for hole in range(9):
            deck = Deck()

            # start round
            # be dealt a hand of 8 cards
            for i in range(8):
                for player in players:
                    player.fill_hand(deck.draw())

            # tee off
            for player in players:
                player.tee_off()

            # create a discard for the first player
            deck.discard(deck.draw())

            playing: bool = True
            first_player_flipped_out: Player = None
            players[0].flip_out() # DEBUG

            # begin taking turns
            while playing:
                for player in players:
                    print(player)
                    # players go around from player that flipped out then hole ends
                    if first_player_flipped_out == player:
                        playing = False
                        break

                    # reshuffle discard pile if needed
                    if deck.cards_remaining() == 0:
                        deck.reshuffle()

                    # player turn
                    # if player.chose_draw_from_deck(deck.get_discard_value()):
                    #     deck.discard(player.turn_draw_from_deck(deck.draw()))
                    # else:
                    #     deck.discard(player.turn_draw_from_discard(deck.draw_from_discard()))

                    # check if player has flipped out
                    if player.is_flipped_out() and first_player_flipped_out is None:
                        first_player_flipped_out = player

            for player in players:
                player.add_to_score(player.score_hand())

            player.get_score()

            # cleanup
            for player in players:
                player.clear_hand()

    main()


def deal_vs_draw():
    deck = Deck()
    deck.deal().print()
    deck.draw().print()


player_scoring()
# deck_reshuffle()
# read_discard()
# flip_out()
# deal_vs_draw()
