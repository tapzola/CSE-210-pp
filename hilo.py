import random

def main():

# define the variables that we already are given
    player_points = 300
    points_won = 100
    points_lost = 75

#make a function that will deal a random card from the 13 cards
    def deal():
        deal = random.randint(1,14)
        return deal

#make a fuction that will pick a random card from the 13 cards
    def pick():
        pick = random.randint(1,14)
        return pick
# create a while loop that you ensure your game keeps playing till user says no or they have 0 points
    playing_game = True
    while playing_game:
        card_deal = deal()
        print(f"The card is {card_deal}")
        question = input("Higher or lower? [h/l]:")
        card_pick = pick()
        print(f"The next card is {card_pick}")
# create if statements to allow your program to do all the major possiblilties that the user may choose.
        if question == "h" and card_deal < card_pick:
            player_points += points_won

        elif question == "h" and card_deal > card_pick:
            player_points -= points_lost

        elif question == "l" and card_deal > card_pick:
            player_points += points_won

        elif question == "l" and card_deal < card_pick:
            player_points -= points_lost

        print(player_points)

        keep_playing = input("Do you want to keep playing:")
        if keep_playing == "n" or player_points == 0:
            playing_game = False
            
if __name__ == "__main__":
    main()
