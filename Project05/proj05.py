###########################################################
# The purpose of this project is to create a poker game
#  that compares two hands of cards and determines the winner.
#  The program will deal two hands of two cards each to two players.
#  It will then deal five community cards.
#  The program will determine the best hand each player can make
#  using their two cards and the five community cards.
#  The program will then compare the two hands and determine the winner.
#  The program will then ask the user if they want to play another hand.
#  If the user says no, the program will end.
#  If the user says yes, the program will deal two new hands of two cards each
# funtion is_flush(cards) will return the best flush hand possible
# funtion is_straight(cards) will return the best straight hand possible
# funtion is_straight_flush(cards) will return the best straight flush hand possible
# funtion is_four_of_a_kind(cards) will return the best four of a kind hand possible
# funtion is_full_house(cards) will return the best full house hand possible
# funtion is_three_of_a_kind(cards) will return the best three of a kind hand possible
# funtion is_two_pair(cards) will return the best two pair hand possible
# funtion is_one_pair(cards) will return the best one pair hand possible
# funtion find_category(hand, community_cards) will return the best possible hand
###########################################################

from cards import Card, Deck

CATEGORIES = {"Straight Flush": 8, "Four of a Kind": 7, "Full House": 6, "Flush": 5, "Straight": 4,
              "Three of a Kind": 3, "Two Pair": 2, "One Pair": 1, "High Card": 0}

ranks_order = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
suits_order = ['♣', '♦', '♥', '♠']

"-" * 40
"Let's play poker!\n"
"Community cards: {}"
"{}: {}"

"TIE with a High Card"
"TIE with a {}: {}"
"{} wins with a {}: {}"

"Deck has too few cards so game is done."
"\n:~ Do you wish to play another hand? (Y or N) ~:"




def card_sort_key(card):
    '''Return a tuple to be used as the key for sorting cards.
    The tuple should have two elements: the first should be an integer
    representing the rank of the card, and the second should be an integer'''
    rank, suit = card.rank(), card.suit()
    rank_index = ranks_order.index(str(rank))
    suit_index = suits_order.index(suits_order[suit - 1])
    return rank_index, suit_index


def find_category(hand, community_cards):
    '''Return the best possible hand category and the cards that make it up.
    The best possible hand category is determined from the 7 cards in the
    hand and community_cards. The cards that make up the best possible hand
    parameters: hand, a list of 2 Card objects representing the player's hand
        community_cards, a list of 5 Card objects representing the community cards'''
    hand = hand + community_cards
    sorted_cards = sorted(hand, key=card_sort_key)
    if is_straight_flush(sorted_cards):
        return "Straight Flush", is_straight_flush(sorted_cards)
    elif is_four_of_a_kind(sorted_cards):
        return "Four of a Kind", is_four_of_a_kind(sorted_cards)
    elif is_full_house(sorted_cards):
        return "Full House", is_full_house(sorted_cards)
    elif is_flush(sorted_cards):
        return "Flush", is_flush(sorted_cards)
    elif is_straight(sorted_cards):
        return "Straight", is_straight(sorted_cards)
    elif is_three_of_a_kind(sorted_cards):
        return "Three of a Kind", is_three_of_a_kind(sorted_cards)
    elif is_two_pair(sorted_cards):
        return "Two Pair", is_two_pair(sorted_cards)
    elif is_one_pair(sorted_cards):
        return "One Pair", is_one_pair(sorted_cards)
    else:
        return "High Card", [sorted_cards[0]]


def is_flush(cards):
    ''' Return the best flush hand possible from the list of cards, or False if there is no flush.
    A flush is 5 or more cards of the same suit. If there are multiple flushes, return the flush with the highest cards.
    parameters: cards, a list of 7 Card objects representing the player's hand and the community cards
    return value: a list of 5 Card objects representing the best flush hand, or False if there is no flush.'''
    the_suits= [card.suit() for card in cards]
    count_suits=[the_suits.count(suit) for suit in the_suits]
    if max(count_suits) >= 5 :
        flush_suit = the_suits[count_suits.index(max(count_suits))]
        flush_cards = [card for card in cards if card.suit() == flush_suit]
        flush_cards.sort(key=lambda x: x.rank())
        return flush_cards[:5]
    return False

def is_straight(cards):
    ''' Return the best straight hand possible from the list of cards, or False if there is no straight.
    A straight is 5 consecutive cards of any suit. If there are multiple straights, return the straight with the highest cards.
    parameters: cards, a list of 7 Card objects representing the player's hand and the community cards
    return value: a list of 5 Card objects representing the best straight hand, or False if there is no straight.
    '''
    the_ranks = [card.rank() for card in cards]
    the_ranks = list(set(the_ranks))
    the_ranks.sort()
    if 1 in the_ranks:
        the_ranks.append(14)
    for i in range(len(the_ranks) - 5):
        if the_ranks[i] == the_ranks[i + 4] - 4:
            x=[card for card in cards if card.rank() in the_ranks[i:i + 5]]
            x.sort(key=lambda x: x.rank())
            return x
    return False

def is_straight_flush(cards):
    ''' Return the best straight flush hand possible from the list of cards, or False if there is no straight flush.
    A straight flush is 5 consecutive cards of the same suit. If there are multiple straight flushes, return the straight flush with the highest cards.
    parameters: cards, a list of 7 Card objects representing the player's hand and the community cards
    return value: a list of 5 Card objects representing the best straight flush hand, or False if there is no straight flush.'''
    cards_rank = [card.rank() for card in cards]
    cards_suit = [card.suit() for card in cards]
    for i in range(1, 5):
        if cards_suit.count(i) >= 5:
            flush_cards = [card for card in cards if card.suit() == i]
            if is_straight(flush_cards):
                x=is_straight(flush_cards)
                x.sort(key=lambda x: x.rank())
                return x
    return False

def is_four_of_a_kind(cards):
    ''' Return the best four of a kind hand possible from the list of cards, or False if there is no four of a kind.
    Four of a kind is 4 cards of the same rank. If there are multiple four of a kinds, return the four of a kind with the highest cards.
    parameters: cards, a list of 7 Card objects representing the player's hand and the community cards
    return value: a list of 4 Card objects representing the best four of a kind hand, or False if there is no four of a kind.'''
    cards_rank = [card.rank() for card in cards]
    for rank in cards_rank:
        if cards_rank.count(rank) == 4:
            x=[card for card in cards if card.rank() == rank]
            x.sort(key=lambda x: x.suit())
            return x
    return False


def is_full_house(cards):
    ''' Return the best full house hand possible from the list of cards, or False if there is no full house.
    A full house is 3 cards of one rank and 2 cards of another rank. If there are multiple full houses, return the full house with the highest cards.
    parameters: cards, a list of 7 Card objects representing the player's hand and the community cards
    return value: a list of 5 Card objects representing the best full house hand, or False if there is no full house.'''
    cards_rank = [card.rank() for card in cards]
    for rank in cards_rank:
        if cards_rank.count(rank) == 3:
            for rank2 in cards_rank:
                if cards_rank.count(rank2) == 2:
                    x=[card for card in cards if card.rank() == rank or card.rank() == rank2]
                    x.sort(key=(lambda x: x.suit()))
                    x.sort(key=(lambda x: x.rank()))
                    return x
    return False

def is_three_of_a_kind(cards):
    ''' Return the best three of a kind hand possible from the list of cards, or False if there is no three of a kind.
    Three of a kind is 3 cards of the same rank. If there are multiple three of a kinds, return the three of a kind with the highest cards.
    parameters: cards, a list of 7 Card objects representing the player's hand and the community cards
    return value: a list of 3 Card objects representing the best three of a kind hand, or False if there is no three of a kind.'''
    cards_rank = [card.rank() for card in cards]
    for rank in cards_rank:
        if cards_rank.count(rank) == 3:
            x=[card for card in cards if card.rank() == rank]
            x.sort(key=lambda x: x.rank())
            return x
    return False


def is_two_pair(cards):
    ''' Return the best two pair hand possible from the list of cards, or False if there is no two pair.
    Two pair is 2 cards of one rank and 2 cards of another rank. If there are multiple two pairs, return the two pair with the highest cards.
    parameters: cards, a list of 7 Card objects representing the player's hand and the community cards
    return value: a list of 4 Card objects representing the best two pair hand, or False if there is no two pair.'''
    cards_rank = [card.rank() for card in cards]
    pairs = []
    for rank in set(cards_rank):
        if cards_rank.count(rank) == 2:
            pair = [card for card in cards if card.rank() == rank]
            pairs.extend(pair)
        if len(pairs) == 4:
            pairs.sort(key=lambda x: x.suit())
            pairs.sort(key=lambda x: x.rank())
            return pairs
    return False

def is_one_pair(cards):
    ''' Return the best one pair hand possible from the list of cards, or False if there is no one pair.
    One pair is 2 cards of the same rank. If there are multiple one pairs, return the one pair with the highest cards.
    parameters: cards, a list of 7 Card objects representing the player's hand and the community cards
    return value: a list of 2 Card objects representing the best one pair hand, or False if there is no one pair.'''
    cards_rank = [card.rank() for card in cards]
    pairs = []
    for rank in set(cards_rank):
        if cards_rank.count(rank) == 2:
            pair = [card for card in cards if card.rank() == rank]
            pairs.extend(pair)
    if pairs:
        pairs.sort(key=lambda x: x.rank())
        pairs.sort(key=lambda x: x.suit())
        return pairs[:2]
    return False

def compare_hands(player1_hand, player2_hand, community_cards,player1,player2):
    '''Return a string indicating the winner of the hand and the category of the winning hand.
    The string should be formatted as follows: "NAME wins with a CATEGORY: CARDS"
    where NAME is the name of the winning player, CATEGORY is the category of the winning hand,
    and CARDS is a list of the cards that make up the winning hand.
    If the hands are tied, return "TIE with a CATEGORY: CARDS"
    where CATEGORY is the category of the tied hands, and CARDS is a list of the cards that make up the tied hands.'''
    player1_category = find_category(player1_hand, community_cards)
    player2_category = find_category(player2_hand, community_cards)
    if CATEGORIES[player1_category[0]] > CATEGORIES[player2_category[0]]:
        return "{} wins with a {}: {}".format(player1, player1_category[0], player1_category[1])
    elif CATEGORIES[player1_category[0]] < CATEGORIES[player2_category[0]]:
        return "{} wins with a {}: {}".format(player2, player2_category[0], player2_category[1])
    else:
        return "TIE with a {}: {}".format(player1_category[0], player1_category[1])



def main():
    game = True
    Deck_of_Cards = Deck()
    Deck_of_Cards.shuffle()
    community_cards = []
    for i in range(5):
        community_cards.append(Deck_of_Cards.deal())
    player1_hand = [Deck_of_Cards.deal() for x in range(2)]
    player2_hand = [Deck_of_Cards.deal() for x in range(2)]
    player1=input(":~ Player 1 ~:")
    player2=input(":~ Player 2 ~:")
    print("-" * 40)
    while game:
        print("Let's play poker!")
        print("\nCommunity cards: {}".format(community_cards))
        print("{}: {}".format(player1,player1_hand))
        print("{}: {}".format(player2,player2_hand))
        print(compare_hands(player1_hand, player2_hand, community_cards,player1,player2))
        if len(Deck_of_Cards)<=7:
            print("Deck has too few cards so game is done.")
            break
        user=input("\n:~ Do you wish to play another hand? (Y or N) ~:")
        if user.lower() == 'n':
            game = False
        else:
            community_cards = []
            for i in range(5):
                community_cards.append(Deck_of_Cards.deal())
            player1_hand = [Deck_of_Cards.deal() for x in range(2)]
            player2_hand = [Deck_of_Cards.deal() for x in range(2)]
            print("-" * 40)
if __name__ == "__main__":
    main()
