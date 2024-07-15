############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import sys
import os
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Count score
def count_score(card_list):
  score = 0
  for card in card_list:
    score += card
  return score
# is_blackjack
def is_blackjack(card_list):
  score = 0
  for card in card_list:
    score += card
  if score == 21:
    return True
  return False
#Check card A is 1 or 11
def count_A_card(A_index, card_list , score):
  if score > 21: 
    card_list[A_index] = 1
    cur_score = count_score(card_list)
  return cur_score

#convert card_name 11 - 13 to 10
def convert_card_name(card_list):
  for i in range(len(card_list)):
    if card_list[i] in [11, 12, 13]:
      card_list[i] = 10
  return card_list

# Check continue get card or not
def get_card(card_list, score):
  next_card = random.randint(1, len(card_list))
  card_list.append(next_card)
  current_score = count_score(card_list)
  for index in range(len(card_list)):
    if(card_list[index] == 11):
      current_score = count_A_card(A_index = index, card_list = card_list , score = current_score)
    if (current_score > 21):
      return current_score
  return current_score  

#game function
def Black_Jack():
  len_card = len(cards)
  player_card = []
  computer_card = []
  player_score = 0
  computer_score = 0
  print(logo)

  for i in range(2):
    player_card.append(random.randint(1, len_card))
    computer_card.append(random.randint(1, len_card))
  # check if exist blackjack
  if (is_blackjack(player_card) and is_blackjack(computer_card)):
    print("Both is blackjack. Draw")
    return
  elif (is_blackjack(player_card)):
    print("You has blackjack!! You win! Congratulations ")
  elif (is_blackjack(computer_card)):
    print("Computer has blackjack!! You Lose! ")

  player_card = convert_card_name(card_list = player_card)
  computer_card = convert_card_name(card_list = computer_card)
  player_score = count_score(card_list = player_card)
  computer_score = count_score(card_list = computer_card)
  
  # print list_card and current score
  print(f"Your card: {player_card}, current score: {player_score}")
  print(f"Computer's first card: {computer_card[0]}")
  
  #Player get Card
  player_get = True
  while player_get:
    choice = input("Type 'y' to get another card, type 'n' to pass:  ").lower()
    if choice == "y":
      player_score = get_card(card_list = player_card, score = player_score)
      print(f"Your card: {player_card}, current score: {player_score}")
      print(f"Computer's first card: {computer_card[0]}")
      if player_score > 21:
        player_get = False
    elif choice == "n":
      player_get = False
  
    
  #Computer get card
  computer_get = True
  while computer_get:
    if computer_score > 21: 
      computer_get = False
    elif computer_score in [21, 20, 19, 18, 17, 16]:
      computer_get = False
    elif computer_score < 16:
      computer_score = get_card(card_list = computer_card, score = computer_score)
    else:
      computer_get = False
    
  #Final step
  print(f"Your final hand: {player_card}, final_score: {player_score}")
  print(f"Computer's final hand: {computer_card}, final_score: {computer_score}")
  if (computer_score > 21 ):
    print("\nComputer went over!! You Win")
  elif (player_score > 21):
    print("\n Your went OVer!! you lose")
  elif (player_score > computer_score):
    print("\nYou win")
  elif (player_score == computer_score):
    print("\nDraw")
  elif (player_score < computer_score):
    print("\nYou Lose")

#Start Game
want_continue_game = True
while want_continue_game:
  player_choice = input("\n\nDo you want to play a game of Blackjack? Type 'y' or 'n':  ")
  if(player_choice == "y"):
    os.system('clear')
    Black_Jack()
  elif(player_choice == "n"):
    want_continue_game = False
  else:
    os.system('clear')
        
