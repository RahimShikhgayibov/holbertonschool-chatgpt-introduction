#!/usr/bin/python3
"""
A simple checkbook program to manage deposits, withdrawals, and balance inquiries.
"""

class Checkbook:
    """
    Function Description:
    A class representing a simple checkbook to keep track of a balance.
    """
    def __init__(self):
        """
        Function Description:
        Initializes the Checkbook instance with a starting balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
        Adds the specified amount to the checkbook balance.

        Parameters:
        amount (float): The amount of money to deposit.

        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function Description:
        Subtracts the specified amount from the balance if funds are sufficient.

        Parameters:
        amount (float): The amount of money to withdraw.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function Description:
        Prints the current checkbook balance.

        Parameters:
        None

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Function Description:
    The main loop that prompts the user for actions and safely handles input.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        
        if action.lower() == 'exit':
            break
            
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                # Extra safeguard: Prevent negative deposits
                if amount <= 0:
                    print("Error: Amount must be greater than zero.")
                else:
                    cb.deposit(amount)
            except ValueError:
                # Catch non-numeric inputs like letters or symbols
                print("Error: Invalid input. Please enter a valid numeric amount.")
                
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                # Extra safeguard: Prevent negative withdrawals
                if amount <= 0:
                    print("Error: Amount must be greater than zero.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                # Catch non-numeric inputs like letters or symbols
                print("Error: Invalid input. Please enter a valid numeric amount.")
                
        elif action.lower() == 'balance':
            cb.get_balance()
            
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()