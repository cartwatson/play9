from deck import Deck
from player import Player


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
                player.fill_hand(deck.deal())

        # tee off
        for player in players:
            player.tee_off()

        # create a discard for the first player
        deck.discard(deck.draw())

        # init loop control bools
        playing: bool = True
        first_player_flipped_out: Player = None

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
                all_played_cards: list[int] = deck.get_discard_values()
                for player in players:
                    all_played_cards.append(player.face_up_cards())

                if player.chose_draw_from_deck(all_played_cards, deck.get_discard_top_card_value()):
                    deck.discard(player.turn_draw_from_deck(deck.draw()))
                else:
                    deck.discard(player.turn_draw_from_discard(deck.draw_from_discard()))

                # check if player has flipped out
                if player.is_flipped_out() and first_player_flipped_out is None:
                    first_player_flipped_out = player

        # score up the round
        for player in players:
            player.flip_out()
            player.add_to_score(player.score_hand())

        # cleanup
        for player in players:
            player.clear_hand()

    # determine who won
    players.sort(key=lambda x: x.get_score(), reverse=True)


if __name__ == "__main__":
    main()
