import cards
''' The basic process is this:
    1) You create a Deck instance, which is filled (automatically) with 52 Card instances
    2) You can deal those cards out of the deck into hands, each hand a list of cards
    3) You then manipulate cards as you add/remove them from a hand
'''
my_deck = cards.Deck()
print("======messy print a deck=====")
print(my_deck)

print("======pretty print a deck=====")
my_deck.display()

my_deck.shuffle()
print("======shuffled deck=====")
my_deck.display()

a_card = my_deck.deal()
print("Dealt card is:",a_card)
print('How many cards left:',len(my_deck))

print("Is the deck empty?",my_deck.is_empty())

# deal some hands and print
hand1_list=[]
hand2_list=[]
for i in range(5):
    hand1_list.append(my_deck.deal())
    hand2_list.append(my_deck.deal())
                      
print("\nHand 1:", hand1_list)
print("Hand 2:", hand2_list)
print()

# take the last card dealt out of each hand
last_card_hand1 = hand1_list.pop()
last_card_hand2 = hand2_list.pop()
print("Hand1 threw down",last_card_hand1, ", Hand2 threw down", last_card_hand2)
print("Hands are now:",hand1_list, hand2_list)

# check the compares (based on rank)
if last_card_hand1 == last_card_hand2:
    print(last_card_hand1, last_card_hand2, "of equal rank")
elif last_card_hand1.rank() > last_card_hand2.rank():
    print(last_card_hand1.rank(), "of higher rank than",last_card_hand2.rank())
else:
    print(last_card_hand2.rank(), "of higher rank than",last_card_hand1.rank())

# check the compares (based on value)
if last_card_hand1.value() == last_card_hand2.value():
    print(last_card_hand1, last_card_hand2, "of equal value")
elif last_card_hand1.value() > last_card_hand2.value():
    print(last_card_hand1, "of higher value than",last_card_hand2)
else:
    print(last_card_hand2, "of higher value than",last_card_hand1)

# check the compares (based on suit)
if last_card_hand1.suit() == last_card_hand2.suit():
    print(last_card_hand1,'of equal suit with',last_card_hand2)
else:
    print(last_card_hand1,'of different suit than',last_card_hand2)

# check the compares (by rank if the same check suit)
if last_card_hand1 < last_card_hand2:
    print(last_card_hand1,'is less than',last_card_hand2)
else:
    print(last_card_hand1,'is higher than',last_card_hand2)

new_hand = sorted(hand1_list)
print(f"original list: {hand1_list}")
print(f"modified hand: {new_hand}")