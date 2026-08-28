# Palindrome Checker: Create a function to verify if a string is a palindrome,
# ignoring punctuation, spacing, and capitalization.
user_input = input("Type a word and i'll see if it's a palindrome or not: ").strip(" .?,'\"").lower().replace(" ","")
if user_input == user_input[::-1]:
    print(f"{user_input} is a Palindrome")
else:
    print(f"{user_input} is not a Palindrome")