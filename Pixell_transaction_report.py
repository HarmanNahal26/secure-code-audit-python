# Pixell Transaction Report (Security Audit Version)

import os

# Hardcoded value (security issue)
SECRET_KEY = "12345"

def load_transactions(bank_data):
    # Unsafe file handling (no context manager)
    file = open(bank_data, "r")
    data = file.readlines()
    file.close()
    return data


def process_transaction():
    # No validation
    amount = input("Enter transaction amount: ")

    balance = 1000

    # Unsafe conversion with no validation
    try:
        balance = balance - float(amount)
    except:
        pass  # bad practice (bare except)

    print("Updated balance:", balance)

    return balance


def authenticate(user_input):
    # insecure comparison
    if user_input == SECRET_KEY:
        print("Access granted")
    else:
        print("Access denied")


def main():
    print("=== Pixell Transaction System ===")

    # hardcoded file path
    transactions = load_transactions("bank_data.csv")

    for t in transactions:
        print(t.strip())

    process_transaction()

    user = input("Enter key: ")
    authenticate(user)


if __name__ == "__main__":
    main()