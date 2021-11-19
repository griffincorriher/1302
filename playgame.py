from Card import Card, Hand, Deck

game_start = False
MAX_POINTS = 21
player = ''

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

#def convert_hand(player):
#    if(player.get_ranks() >=11):
        

def hit(player):
    #add another card to hand, sum cards in hand and return value
    player.add(game_deck.deal())
    points = sum(player.get_ranks())
    return points
    
def stand(player):
    #return hand numerical value after standing
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
    for name, i in zip(player_names, hands_list):
        print(name,"'s hand:\n",i, "\n")
    
## Running Code ##    
player = input("What is your name?\n")
#Input how many computer opponents not including dealer
game_deck = Deck()
game_deck.shuffle()
player_names = ['Dealer', player, 'Computer1', 'Computer2']
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
computer1_hand = all_hands[2]
computer2_hand = all_hands[3]

hands_list = [dealer_hand, player_hand, computer1_hand, computer2_hand]

display_hands()


print("All hands have been dealt")


hit(player_hand)
display_hands()

#play = restart()
