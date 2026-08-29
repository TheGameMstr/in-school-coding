# Task: Write a function that takes a string.
# Return the total vowel count and a new string where all vowels are replaced with a *.
def vowel_replament(user_str):
    vowel_list = ["e","i","o","a","u"]
    new_str = ""
    for let in user_str:
        if let.lower() in vowel_list:
            new_str += "*"
        else:
            new_str += let
    return new_str
user_input = str(input("Give me a word and i'll replace the vowels with *.\n-> "))
print(vowel_replament(user_input))