from Cards.Card import Card, Rank

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):
    rank_order = [Rank.ACE, Rank.KING, Rank.QUEEN, Rank.JACK, Rank.TEN, Rank.NINE, Rank.EIGHT, Rank.SEVEN,
                  Rank.SIX, Rank.FIVE, Rank.FOUR, Rank.THREE, Rank.TWO]
    count_rank = {}
    count_suits = {}
    suits = []
    ranks = []
    for card in hand:
        ranks.append(card.rank)
        suits.append(card.suit)
    for suit in suits:
        if suit not in count_suits:
            count_suits[suit] = 1
        else:
            count_suits[suit] += 1

    for rank in ranks:
        if rank not in count_rank:
            count_rank[rank] = 1
        else:
            count_rank[rank] += 1
    four_of_a_kind = False
    flush = False
    straight = False
    three_of_a_kind = False
    one_pair = False
    quantity_one_pair = 0
    for rank in count_rank:
        if count_rank[rank] == 4:
            four_of_a_kind = True
        if count_rank[rank] == 3:
            three_of_a_kind = True
        if count_rank[rank] == 2:
            one_pair = True
            quantity_one_pair += 1
    for suit in count_suits:
        if count_suits[suit] >= 5:
            flush = True
    def rank_index(i):
        return rank_order.index(i)
    ranks.sort(key=rank_index)
    first_index = rank_index(ranks[0])
    if ranks == rank_order[first_index:first_index+5]:
        straight = True
    if straight and flush:
        return "Straight Flush"
    elif four_of_a_kind:
        return "Four of a Kind"
    elif three_of_a_kind and one_pair:
        return "Full House"
    elif flush:
        return "Flush"
    elif straight:
        return "Straight"
    elif three_of_a_kind:
        return "Three of a kind"
    elif quantity_one_pair == 2:
        return "Two Pair"
    elif one_pair:
        return "One Pair"
    else:
        return "High Card" # If none of the above, it's High Card
