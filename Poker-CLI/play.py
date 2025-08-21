import random

#  Deck
suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def create_deck():
    return [f"{rank}{suit}" for suit in suits for rank in ranks]

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

#  Deal Cards
def deal_hole_cards(deck, players):
    for p in players:
        if p["active"]:
            p["hand"] = [deck.pop(), deck.pop()]

def deal_community_cards(deck):
    deck.pop()  # burn before flop
    flop = [deck.pop(), deck.pop(), deck.pop()]
    deck.pop()  # burn before turn
    turn = [deck.pop()]
    deck.pop()  # burn before river
    river = [deck.pop()]
    return flop, turn, river

#  Betting with hand/board/exit options
def betting_round(players, pot, current_bet=0, min_bet=10, community_cards=None):
    for p in players:
        if not p["active"] or p["folded"]:
            continue

        while True:
            print(f"\n{p['name']}'s turn. Balance: {p['balance']} chips")
            print(f"Current bet to call: {current_bet}")
            action = input("Choose action (check/call/raise/fold/hand/board/exit): ").strip().lower()

            if action == "hand":
                print(f"👉 {p['name']}'s hand: {p['hand']}")
                continue
            elif action == "board":
                print(f"👉 Board so far: {community_cards or 'None'}")
                continue
            elif action == "exit":
                print(f"{p['name']} has exited the game.")
                p["active"] = False
                p["folded"] = True
                break
            elif action == "fold":
                p["folded"] = True
                print(f"{p['name']} folds.")
                break
            elif action == "check":
                if current_bet > 0:
                    print("Can't check—must call or fold.")
                    continue
                print(f"{p['name']} checks.")
                break
            elif action == "call":
                bet = min(current_bet, p["balance"])
                p["balance"] -= bet
                pot += bet
                print(f"{p['name']} calls {bet}.")
                break
            elif action == "raise":
                try:
                    raise_amount = int(input(f"Enter raise amount (min {min_bet}): "))
                except ValueError:
                    print("Invalid amount.")
                    continue
                bet = min(current_bet + raise_amount, p["balance"])
                p["balance"] -= bet
                pot += bet
                current_bet = bet
                print(f"{p['name']} raises to {bet}.")
                break
            else:
                print("Invalid action.")
                continue

        # Check active players count after each action
        active_players = [x for x in players if x["active"] and not x["folded"]]
        if len(active_players) == 1:
            winner = active_players[0]
            print(f"\nOnly {winner['name']} remains. {winner['name']} wins the pot of {pot} chips!")
            exit(0)  # Exit the entire game

    return pot, current_bet

#  Game
def play_poker(num_players=2, starting_balance=1000):
    players = [
        {"name": f"Player {i+1}", "balance": starting_balance, "hand": [], "folded": False, "active": True}
        for i in range(num_players)
    ]

    deck = shuffle_deck(create_deck())
    deal_hole_cards(deck, players)

    for p in players:
        if p["active"]:
            print(f"{p['name']} hand: {p['hand']} (Balance: {p['balance']})")

    pot = 0
    community_cards = []

    # Pre-flop
    print("\n--- Pre-Flop Betting ---")
    pot, current_bet = betting_round(players, pot, community_cards=community_cards)

    # Flop
    flop, turn, river = deal_community_cards(deck)
    community_cards = flop[:]
    print(f"\nFlop: {flop}")
    pot, current_bet = betting_round(players, pot, community_cards=community_cards)

    # Turn
    community_cards += turn
    print(f"\nTurn: {turn}")
    pot, current_bet = betting_round(players, pot, community_cards=community_cards)

    # River
    community_cards += river
    print(f"\nRiver: {river}")
    pot, current_bet = betting_round(players, pot, community_cards=community_cards)

    print(f"\nPot size: {pot}")
    print("Showdown (hand evaluation not yet implemented).")

#  Overall Loop
if __name__ == "__main__":
    while True:
        n = int(input("Enter number of players (2-6): "))
        play_poker(n)
        if input("\nPlay again? (y/n): ").strip().lower() != "y":
            break
