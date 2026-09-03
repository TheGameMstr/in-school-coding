# Character Frequency Map: Take a string input and return a dictionary
# showing exactly how many times each character appears.
user_input = "hello world"
def freq_map_space(user_input):
    freq_dict = {}
    for let in user_input:
        if let not in freq_dict.keys():
            freq_dict[let] = 1
        else:
            freq_dict[let] += 1
    return freq_dict

def freq_map(user_input):
    user_input = user_input.replace(" ","")
    freq_dict = {}
    for let in user_input:
        if let not in freq_dict.keys():
            freq_dict[let] = 1
        else:
            freq_dict[let] += 1
    return freq_dict

print(freq_map_space(user_input))
print(freq_map(user_input))