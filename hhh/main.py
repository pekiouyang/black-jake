import random

# Create a deck of cards (no jokers)
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

# Shuffle the deck
random.shuffle(deck)

# Function to calculate the total score of a hand
def calculate_hand(hand):
    total = sum(hand)
    # If the total is greater than 21 and there's an Ace (11), treat Ace as 1
    aces = hand.count(11)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# Deal a card from the deck
def deal_card(deck):
    return deck.pop()

# Display the current state of the game
def display_game_state(player_hand, dealer_hand, hide_dealer_card=True):
    print(f"Player's hand: {player_hand}, Total: {calculate_hand(player_hand)}")
    if hide_dealer_card:
        print(f"Dealer's hand: [{dealer_hand[0]}, ?]")
    else:
        print(f"Dealer's hand: {dealer_hand}, Total: {calculate_hand(dealer_hand)}")

# Main game loop
def play_blackjack():
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # Player's turn
    while True:
        display_game_state(player_hand, dealer_hand)
        choice = input("Do you want to 'hit' or 'stand'? ").lower()
        if choice == 'hit':
            player_hand.append(deal_card(deck))
            if calculate_hand(player_hand) > 21:
                display_game_state(player_hand, dealer_hand, hide_dealer_card=False)
                print("Player busts! Dealer wins.")
                return
        elif choice == 'stand':
            break
        else:
            print("Invalid input. Please type 'hit' or 'stand'.")

    # Dealer's turn
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

    # Final game state
    display_game_state(player_hand, dealer_hand, hide_dealer_card=False)

    # Determine the winner
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)

    if dealer_total > 21:
        print("Dealer busts! Player wins.")
    elif player_total > dealer_total:
        print("Player wins!")
    elif player_total < dealer_total:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Start the game
if __name__ == "__main__":
    play_blackjack()