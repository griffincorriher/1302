from Card import Card, Hand, Deck

play = True
max_points = 21


def restart():
    play = True
    print("Do you want to play blackjack?\n")
    x = input("Enter Y for Yes and N for No: \n")
    if x.upper() == "Y":
      print('Starting game!')
      play = True
      game_deck = Deck()
      game_deck.shuffle()
      player_hand = Hand()
      player_hand.add(game_deck.deal())
      player_hand.add(game_deck.deal())
      print(player_hand)
    elif x.upper() == "N":
      print('\nThank you!')
      play = False    
    else:
      print("Please enter Y or N")
      restart()
    return play  

play = restart()    
while(play == True):
    
    
    
    play = restart()
