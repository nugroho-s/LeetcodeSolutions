class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        shuffled_deck = [deck[0]]
        for i in range(1, len(deck)):
            card = deck[i]
            temp = shuffled_deck[-1]
            shuffled_deck = shuffled_deck[:-1]
            shuffled_deck.insert(0,temp)
            shuffled_deck.insert(0, card)
        return shuffled_deck
