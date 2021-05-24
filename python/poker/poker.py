from typing import Callable, Dict, List, Tuple

Card = Tuple[int, str] # rank, suit
Hand = List[Card] 

ranks: Dict[str, int] = {
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, 
    '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

def best_hands(raw_hands: List[str]) -> List[str]:
    hands: List[Hand] = list(map(_to_hand, raw_hands))
    hand_rankings: List[Tuple[int, Hand]] = []
    for hand in hands:
        counts: Dict[int, int] = _count_cards(hand)
        hand_rank: Tuple[int, Hand] = (0, hand,)
        for rank, is_rank in hand_ranks.items():
            if is_rank(hand, counts):
                hand_rank[0] = rank
        hand_rankings.append(hand_rank)
    hand_rankings = sorted(hand_rankings, key=lambda ranking: ranking[0], reverse=True)
    print(f"Hand Rankings: {hand_rankings}")
    return [" ".join(f"{cards[0]}{cards[1]}" for cards in hand_rankings[0][1])]

def _to_hand(hand: List[str]) -> Hand:
    return [(ranks[x[0]], x[1]) if len(x) == 2 else (ranks[x[:2]], x[2]) for x in hand.split()]

def _count_cards(hand: Hand) -> Dict[int, int]:
    counts: Dict[int, int] = dict()
    for card in hand:
        counts[card[0]] = counts.get(card[0], 0) + 1
    return counts

def _count_multiples(counts: Dict[int, int], size: int, total: int) -> bool:
    return len(list(count for _, count in counts.items() if count == size)) == total

def _is_one_pair(hand: Hand, counts: Dict[int, int]) -> bool:
    return _count_multiples(counts, 2, 1)

def _is_two_pair(hand: Hand, counts: Dict[int, int]) -> bool:
    return _count_multiples(counts, 2, 2)

def _is_trips(hand: Hand, counts: Dict[int, int]) -> bool:
    return _count_multiples(counts, 3, 1)

def _is_quads(hand: Hand, counts: Dict[int, int]) -> bool:
    return _count_multiples(counts, 4, 1)

def _is_full_house(hand: Hand, counts: Dict[int, int]) -> bool:
    return _count_multiples(counts, 2, 1) and _count_multiples(counts, 3, 1)

def _is_flush(hand: Hand, counts: Dict[int, int]) -> bool:
    return len(set([card[1] for card in hand])) == 1

def _is_straight(hand: Hand, counts: Dict[int, int]) -> bool:
    print(f"hand: {hand}")
    ordered: List[int] = sorted([card[0] for card in hand])
    if ordered[4] - ordered[0] == 4:
        return True
    return ordered == [2, 3, 4, 5, 14]

def _is_straight_flush(hand: Hand, counts: Dict[int, int]) -> bool:
    return _is_straight(hand, counts) and _is_flush(hand, counts)

hand_ranks: Dict[int, Callable[[Hand, Dict[int, int]], bool]] = {
    1: _is_one_pair,
    2: _is_two_pair,
    3: _is_trips,
    4: _is_straight,
    5: _is_flush,
    6: _is_full_house,
    7: _is_quads,
    8: _is_straight_flush,
}