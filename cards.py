def Cards_Game():
    # create a card game
    # create a list of cards
    cards=["King","Queen","Joker","Ace","Heart","Flower","Diamond","Spade"]
    # set the initial points to be zero
    points=0
    # define the number of times we will play the game
    for x in range(6):
        # import random to shuffle items in the list
        import random
        random.shuffle(cards)
        print("Current card is",cards[0]) # pick the first card
        # remove the current card
        cards.remove(cards[0])
        random.shuffle(cards)
        # let the player guess next card at position 0
        answer=str(input("Can you guess the next card: "))
        # check if the answer is correct
        if answer==cards[0]:
            print("Correct!!",cards[0])
            points=points+3 #award points
        else:
            print("It's wrong!! card was",cards[0])
    print("Game Over. You scored",points)
    if points>=9:
        print("Congratulations!!. Next level unlocked")
    else:
        print("Come on, you can do better than this")
Cards_Game()