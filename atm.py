
# ATM Simulation with PIN Change Feature

# Initialize account details
account_balance = 1000  # Initial balance
pin_code = 1234          # Predefined PIN code

# Function to display the menu
def display_menu():
    print("\nWelcome to the ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Exit")

# Function to check balance
def check_balance():
    print(f"Your current balance is: ${account_balance}")

# Function to deposit money
def deposit_money():
    global account_balance  # Use the global variable
    amount = float(input("Enter the amount to deposit: $"))
    if amount > 0:
        account_balance += amount
        print(f"${amount} deposited successfully.")
    else:
        print("Deposit amountis  must be positive.")

# Function to withdraw money
def withdraw_money():
    global account_balance  # Use the global variable
    amount = float(input("Enter the amount to withdraw: $"))
    if amount > 0:
        if amount <= account_balance:
            account_balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")
    else:
        print("Withdrawal amount is must be positive.")

# Function to change the PIN
def change_pin():
    global pin_code  # Use the global variable
    new_pin = int(input("Enter your new PIN: "))
    pin_code = new_pin  # Update the PIN
    print("Your PIN has been changed successfully.")

# Main function to run the ATM
def main():
    # Prompt user for PIN
    entered_pin = int(input("Please enter your PIN: "))
    
    # Check if entered PIN is correct
    if entered_pin == pin_code:
        while True:
            display_menu()  # Show the menu
            choice = input("Select an option between (1-5): ")
            
            if choice == '1':
                check_balance()  # Check balance
            elif choice == '2':
                deposit_money()   # Deposit money
            elif choice == '3':

            elif choice == '4':
                change_pin()      # Change PIN
            elif choice == '5':
                print("Thank you for using the ATM. Goodbye!")
                break  # Exit the loop
            else:
                print("Invalid selection. Please choose again.")
    else:
        print("Incorrect PIN. Access denied.")

# Run the ATM program
if __name__ == "__main__":
    main()