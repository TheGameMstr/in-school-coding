# Valid AnagramTask:
# Write a function that takes two strings and returns True if they are anagrams
# (contain the exact same letters in a different order) and False otherwise.
def VaildAnagram(word1,word2):
    word1 = word1.lower().replace(" ",""); word2 = word2.lower().replace(" ","")
    if sorted(word1) == sorted(word2):
        return f"{word1} & {word2} are anagrams"
    else:
        return f"{word1} & {word2} are not anagrams"
print(VaildAnagram("cat","act"))    