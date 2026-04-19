# Pixell Transaction Report (Security Audit Version)

import os

# 1. Hardcoded secret (Sensitive Data Exposure)
SECRET_KEY = "12345"


def load_transactions(bank_data):
    # 2. Path traversal vulnerability (no validation on file path)
    file = open(bank_data, "r")  # no context manager
    data = file.readlines()
    file.close()
    return data


def process_transaction():
    # 3. No input validation
    amount = input("Enter transaction amount: ")

    balance = 1000

    # 4. Bare except (error handling issue)
    try:
        balance = balance - float(amount)
    except:
        pass

    print("Updated balance:", balance)
    return balance


def authenticate(user_input):
    # 5. Insecure authentication (plain text comparison)
    if user_input == SECRET_KEY:
        print("Access granted")
    else:
        print("Access denied")


def run_system_command():
    # 6. Command Injection vulnerability
    cmd = input("Enter system command: ")
    os.system(cmd)   # VERY unsafe


def view_user_file():
    # 7. Arbitrary file read (Broken Access Control)
    filename = input("Enter filename to view: ")
    with open(filename, "r") as f:
        print(f.read())


def main():
    print("=== Pixell Transaction System ===")

    # Hardcoded file path
    transactions = load_transactions("bank_data.csv")

    for t in transactions:
        print(t.strip())

    process_transaction()

    user = input("Enter key: ")
    authenticate(user)

    # Extra vulnerable features
    run_system_command()
    view_user_file()


if __name__ == "__main__":
    main()