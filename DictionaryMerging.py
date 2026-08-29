dict1 = {"banna":10, "apple":5, "fruit":5000}
dict2 = {"banna":5, "apple":5,"vegi":0}
def same_keys(dict1,dict2):
    new_dict = {}
    same_key_count = 0
    for key in dict1.keys():
        if key in dict2:
            new_dict[key] = (dict1[key] + dict2[key])
            same_key_count += 1
    return f"Number of same keys: {same_key_count}\nKeys and totals: {new_dict}"
print(same_keys(dict1,dict2))
        