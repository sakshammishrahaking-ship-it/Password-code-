# Password Strength Checker
# It checks a password, gives a score, and tells how to make it stronger.
# The password is never saved or printed anywhere.

import getpass  # hides the password while you type it

# very common passwords that attackers try first
COMMON_PASSWORDS = [
    "password", "123456", "12345678", "123456789", "qwerty",
    "abc123", "admin", "letmein", "iloveyou", "welcome",
]

SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>?/|"


def check_password(password):
    score = 0   # goes up for every good thing in the password
    tips = []   # advice for the user

    # 1. common password check (these are weak no matter what)
    if password.lower() in COMMON_PASSWORDS:
        return 0, ["This is one of the most common passwords, choose another one"]

    # 2. length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        tips.append("Use 12 or more characters for a stronger password")
    else:
        tips.append("Use at least 8 characters")

    # 3. character types
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in SYMBOLS for c in password)

    if has_lower:
        score += 1
    else:
        tips.append("Add lowercase letters")

    if has_upper:
        score += 1
    else:
        tips.append("Add uppercase letters")

    if has_digit:
        score += 1
    else:
        tips.append("Add numbers")

    if has_symbol:
        score += 1
    else:
        tips.append("Add symbols like ! @ # $")

    # 4. same character repeated 3 times in a row (like "aaa" or "111")
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            score -= 1
            tips.append("Avoid repeating the same character 3 times in a row")
            break

    return max(score, 0), tips


def get_rating(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    elif score == 5:
        return "Strong"
    else:
        return "Very Strong"


def main():
    print("===== PASSWORD STRENGTH CHECKER =====")
    print("Press Enter without typing anything to exit.\n")

    while True:
        password = getpass.getpass("Enter a password to check: ")

        if password == "":
            print("Bye!")
            break

        score, tips = check_password(password)

        print("Score  :", score, "/ 6")
        print("Rating :", get_rating(score))

        if tips:
            print("Tips:")
            for tip in tips:
                print(" -", tip)
        print()


main()
