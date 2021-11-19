from Card import Card, Hand, Deck

play = True
game_start = False
max_points = 21
player = ''
hands = {}

def restart():
    play = True
    print("Do you want to play blackjack?\n")
    x = input("Enter Y for Yes and N for No: \n")
    if x.upper() == "Y":
      print('Starting game!')
      play = True
    elif x.upper() == "N":
      print('\nThank you!')
      play = False    
    else:
      print("Please enter Y or N")
      restart()
    return play  

def initialize_game():
    game_start = True
    player = input("What is your name?\n")
    #Input how many computer opponents not including dealer
    game_deck = Deck()
    game_deck.shuffle()
    
    players = [player, 'Dealer', 'Computer1', 'Computer2']
    all_hands = []
    for i in range(len(players)):
        players[i] = Hand()
        players[i].add(game_deck.deal())
        players[i].add(game_deck.deal())
        all_hands.append(players[i])
        
    player_hand = all_hands[0]
    dealer_hand = all_hands[1]
    computer1_hand = all_hands[2]
    computer2_hand = all_hands[3]
    print(player_hand)
    player_hand.PrintWithIndexes()
    print(player_hand)

    #create player hand
#    player_hand = Hand()
#    player_hand.add(game_deck.deal())
#    player_hand.add(game_deck.deal())

    #create dealer hand
#    dealer_hand = Hand()
#    dealer_hand.add(game_deck.deal())
#    dealer_hand.add(game_deck.deal())

    #create computer hands for every n computer players
    #they didn't specify how many players, we could put
    #into for loop to make 'n' number of players but I think we just make 2
#    computer1_hand = Hand()
#    computer1_hand.add(game_deck.deal())
#    computer1_hand.add(game_deck.deal())
    
#    computer2_hand = Hand()
#    computer2_hand.add(game_deck.deal())
#    computer2_hand.add(game_deck.deal())

#    print(player_hand)
    print("All hands have been dealt")
    return game_start

def play_game():
    print()

def hit(player):
    #add another card to hand
    print('ok')
    
def stand(player):
    #return hand numerical value
    print('ok')
    
def compare(player):
    #compare player hands
    print('ok')


    
    
    
play = restart()    
while(play == True):
    game_start = initialize_game()
    print(game_start)
    while(game_start == True):
        play_game()
    
    
       
    
    
        #play = restart()

