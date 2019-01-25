import random

print("Welcome to Dunkin' Donuts new recruit! You have your first customer already. Tend to her.")
print("-------------------------------")
#Introduction to the player of the game.

turn = 0
while turn < 3:
  yeo = 0 #Just to have a variable that is true.
  correctorder = [] #Ordered list of what the actually correct order will be based on what customer asks for.
  yourorder = [] #Ordered list of what the player makes during gameplay.

  orders = ['coffee', 'latte', 'americano', 'hot chocolate'] #Different drinks that a customer can order.
  ordersrandom = random.choice(orders) #Customer randomly orders one of the drink choices.
  ordersize = ['small', 'medium', 'large'] #Choice of what size the drink can be.
  ordersizerandom = random.choice(ordersize) #Customer randomly selects a size for their drink.
  correctorder.append(f"{ordersizerandom} cup")

  if ordersrandom == 'coffee':
    correctorder.append('cream and sugar')
    correctorder.append('coffee')
  elif ordersrandom == 'latte':
    correctorder.append('expresso shot')
    correctorder.append('steamed milk')
  elif ordersrandom == 'americano':
    correctorder.append('expresso shot')
    correctorder.append('water')
  elif ordersrandom == 'hot chocolate':
    correctorder.append('hot chocolate')
  else:
    print("wait a minute...")
  #Depending on what the customer orders, the correct item order condition will be made to win.

  additions = ['cream and sugar', 'expresso shot', 'hot chocolate', 'coffee', 'water', 'steamed milk']
 # List of what items can be added to a drink.

  print(f"Customer: Hey there. Can I get a {ordersizerandom} {ordersrandom}?")
  if ordersrandom == 'coffee':
    print("You: Light and sweet?")
    print("Customer: Yes please, and hurry up will you.")
  else:
    pass
  # If customer orders coffee, it will always be light and sweet.
  print("You: Yeah sure lemme get it.")
  print(" ")
  print(f"Conscience: Okay... what cup size do I get for a {ordersizerandom} order?:")
  cupsize = input(ordersize)
  yourorder.append(f"{cupsize} cup")
  print(f"What you have:{yourorder}")
 # Customer just orders something.

  while yeo == 0:
    print(" ")
    print("Alright. Now what do I add next?")
    print(additions)
    nextadd = input()
    yourorder.append(nextadd)
    print(f"What you have: {yourorder}")
    print(" ")

    g = 0
    while g < 7:

        doneornot = input("Am I done?")
        if doneornot == 'no':
            g = g + 7
        elif doneornot == 'yes':
            print(" ")
            print("You: Okay ma'am, here's your order.")
            g = g + 7
            yeo = yeo + 1
        else:
            print("yes or no fool")
  # After adding an item to the drink, player is given option to finish or keep adding items.

  if yourorder == correctorder:
    print("Customer: Yes, thank you!")
    print("You: Alright! Now, I can help who's next.")
    print("╱╱┏╮")
    print("╱╱┃┃")
    print("▉━╯┗━╮")
    print("▉┈┈┈┈┃")
    print("▉╮┈┈┈┃")
    print("╱╰━━━╯")
    print("----------------------------------------")
    print(" ")
  else:
    print("Customer: Ayo! This is not what I ordered. Let me speak to your manager so you can be fired immediately. Your boss will be hearing a handful from me, the customer, and the customer is always right. Since I'm the customer I can just say you are fired right now and you have to leave because I am always right. This is unbelievable and unexcusable. I am never coming to this Dunkin' again. This was the worst experience of my life; worse than when my husband left me for the second time. Now I have to hold the kids and pay for their insurance. Life could not be going worse and you ruined it by messing up my order that I order every single day. I used to be a loyal customer but now I will leave and never come back. This is a disrespect to the whole Dunkin' Donuts customer community. I will tell all my friends and family. Good day you fool. ")
    print("You: Whatever bro. Keep it moving.")
    print("     .-TTTTTT-.")
    print("   .' \\\    // '.")
    print("  /   O      O   \\")
    print(" :       __       :")
    print("  \  .- `  ` -.  /")
    print("   '.          .'")
    print("     '-......-'")
    print("----------------------------------------")
    print(" ")
 # If customer is served drink in correct order and everything, player wins and customer just leaves.
  turn += 1

