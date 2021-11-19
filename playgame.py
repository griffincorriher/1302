from Card import Card, Hand, Deck

game_start = False
MAX_POINTS = 21
player = ''
player_points = []
NUMBER_OPPONENTS = 2

def restart():
    global play
    print("Do you want to play blackjack?\n")
    x = input("Enter Y for Yes and N for No: \n")
    if x.upper() == "Y":
      print('Starting game!')
      play = True
    elif x.upper() == "N":
      print('\nThank you!')
      play = False    
    else:
      restart()
    return play  

def play_game():
    print()       

def hit(hand):
    #add another card to hand, sum cards in hand and return value
    hand.add(game_deck.deal())
    points = sum(hand.get_ranks())
    sum_points()
    display_hands()
    return points
    
def stand(player):
    #return hand numerical value after standing
    stand = True
    points = sum(player.get_ranks())
    return points
    
def compare(player):
    #compare player hands against max_points
    print('ok')

def display_dealer_hand():
    dealer_hand.add(dealers_first_card)
    points = sum(dealer_hand.get_ranks())
    return points

def display_hands():
    #Have logic here if players stand or bust, add dealer card back into hand    
    for name, i in zip(player_names, hands_list):
        print(name,"'s hand:\n",i, "\n")
    sum_points()    
    print("_"*20)

def sum_points():
    player_points.clear()
    for name, i in zip(player_names, hands_list):
        cards = i.get_ranks()
        card_values = []
        card_sum = 0
        for card in cards:
            if(card>=11):
                card = 10
            card_values.append(card)
        player_points.append(sum(card_values))

    if(player_points > MAX_POINTS):
        done_playing = True
            
def display_points():
    for name, i in zip(player_names, player_points):
        print(name,"'s points:",i, "\n")    
#def dealer_play():
    
    
    
##START CODE##
player = input("What is your name?\n")

#Shuffle deck
game_deck = Deck()
game_deck.shuffle()

#Create players
player_names = ['Dealer', player]
for n in range(NUMBER_OPPONENTS):
    name = 'Computer%s' % str(int(n)+1)
    player_names.append(name)

#Create player hands
hands = [None] * len(player_names)
all_hands = []

for i in range(len(hands)):
    hands[i] = Hand()
    hands[i].add(game_deck.deal())
    hands[i].add(game_deck.deal())
    all_hands.append(hands[i])

dealer_hand = all_hands[0]
dealers_first_card = dealer_hand.discard_top()    
player_hand = all_hands[1]

#for loop to create 'n' computer hands
computer1_hand = all_hands[2]
computer2_hand = all_hands[3]

hands_list = [dealer_hand, player_hand, computer1_hand, computer2_hand]
#hands_list = [dealer_hand, player_hand]
#hands_list.append() to append hands into list

#Running game code/while loop
display_hands()

hit(dealer_hand)
print(player_points)
hit(player_hand)
print(player_points)
print("All hands have been dealt")

#When all players stay or bust, dealer shows full hand then stays or hits

#play = restart()
