deck_of_cards = input().split()
count_of_shuffles = int(input())
for i in range(count_of_shuffles):
    middle_of_deck = len(deck_of_cards) // 2
    left_deck = deck_of_cards[0:middle_of_deck]
    right_deck = deck_of_cards[middle_of_deck::]
    final_deck = []
    for index in range(len(right_deck)):
        final_deck.append(left_deck[index])
        final_deck.append(right_deck[index])
    deck_of_cards = final_deck
print(final_deck)
