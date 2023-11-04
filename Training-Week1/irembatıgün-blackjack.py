import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
card_values = {'J': 10, 'Q': 10, 'K': 10, 'A': 11}
name = input("What is your name? ")


class Player():
  #defining constructure
  def __init__(self, name, hand, score, balance):
    self.name = name
    self.hand = hand
    self.score = score
    self.balance = balance


def showhand(player):
  calc_score(player)
  print(f"{player.name}'s hand: {player.hand}")
  print(f"{player.name}'s score: {player.score}")


def calc_score(player):
  score = 0
  num_aces = 0
  # iterate through the cards in the player's hand
  for card in player.hand:
    if card == 'A':
      num_aces += 1
    score += card_values.get(card, card)

  while num_aces > 0 and score > 21:
    score -= 10
    num_aces -= 1

  player.score = score


def drawcard(player, number_of_cards):
  player.hand.extend(random.choices(cards, k=number_of_cards))
  calc_score(player)


def choose():
  print("Welcome to Blackjack " + name)
  print(
      "1. Start Game\n2. Show Balance\n3. Quit Game\nPlease enter your choice: "
  )
  choice = input()

  if choice == "1":
    game()
  elif choice == "2":
    showbalance()
  elif choice == "3":
    quit_game()
  else:
    choose()


def calcwin(user, comp, bet):
  for i in range(1):
    if (user.score > 21):
      print("You busted!!!")
      user.balance -= bet
      comp.balance += bet

    elif (user.score == 21):
      print("You got 21. You win!!!")
      user.balance += bet
      comp.balance -= bet

    else:
      while (comp.score <= 16):
        drawcard(comp, 1)

      if (comp.score > 21):
        print("Computer busted!!!")
        user.balance += bet
        comp.balance -= bet

      elif (comp.score > user.score):
        print("Computer wins!!!")
        user.balance -= bet
        comp.balance += bet

      elif (comp.score < user.score):
        print("You win!!!")
        user.balance += bet
        comp.balance -= bet

      else:
        print("It's a tie!!!")

  showhand(user)
  showhand(comp)
  showbalance()
  choose()


def game():
  bet = int(input("How much would you like to bet? "))

  user.score = 0
  comp.score = 0
  user.hand.clear()
  comp.hand.clear()

  drawcard(user, 2)
  drawcard(comp, 2)

  if bet > user.balance:
    print("Bet amount exceeds your balance.")
    user.hand.clear()
    comp.hand.clear()
    game()

  showhand(user)
  print("Computer's first card: ", comp.hand[0])

  while (user.score < 21):
    decision = input("Type 'y' to get another card 'n' to pass: ")

    if (decision == "y"):
      drawcard(user, 1)
      showhand(user)
      if (comp.score <= 17):
        drawcard(comp, 1)

    elif (decision == "n"):

      calcwin(user, comp, bet)
    else:
      print("Invalid input.")

  calcwin(user, comp, bet)


def showbalance():
  print("Your balance is: " + str(user.balance))
  choose()


def quit_game():
  print("Thanks for playing!")
  exit()

# Creating Player objects
user = Player(name, [], 0, 1000)
comp = Player("comp", [], 0, 1000)

choose()
