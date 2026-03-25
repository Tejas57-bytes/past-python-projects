#pyhon slot game

import random

def spin_slot_machine():
    symbols = ['🍒', '🍋', '🍊', '🍉', '⭐', '💎']
    return [random.choice(symbols) for _ in range(3)]

def print_slot_machine_result(result):
    print("Result:", ' '.join(result))

def pay_out_multiplier(symbol):
    multipliers = {
        '🍒': 2,
        '🍋': 3,
        '🍊': 4,
        '🍉': 5,
        '⭐': 10,
        '💎': 20
    }
    return multipliers.get(symbol, 1)

def play_slot_game():
    balance = 100
    print("************************************")
    print("Welcome to the Slot Machine Game!")
    print('🍒', '🍋', '🍊', '🍉', '⭐', '💎')
    print(f"Your starting balance is: ${balance}")
    print("************************************")
    
    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Enter your bet amount: ")
        if not bet.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue
        bet = int(bet)
        if bet <= 0:
            print("Bet must be greater than zero.")
            continue
        if bet > balance:
            print("You cannot bet more than your current balance.")
            continue

        balance -= bet
        result = spin_slot_machine()
        print_slot_machine_result(result)
        if result[0] == result[1] == result[2]:
            multiplier = pay_out_multiplier(result[0])
            winnings = bet * multiplier
            balance += winnings
            print(f"Congratulations! You won ${winnings} with a multiplier of {multiplier}x for {result[0]}!")
        else:
            print("Sorry, you didn't win this time.")
        print("************************************")
    print("Game over! Your final balance is: $", balance)
    
if __name__ == "__main__":
    play_slot_game()

    