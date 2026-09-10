def CeasarDecoder(user_string,user_num = 1):
    ### this turns leters into 1-26 useing ascii but trimed down for the 1-26 alphbet
    alphabet_dict = {chr(i): i - 96 for i in range(97, 123)}
    trans_askii_list = []
    for let in user_string.lower():
        if let in alphabet_dict.keys():
            trans_askii_list.append(alphabet_dict[let])
        else:
            trans_askii_list.append(let)
    ### this turns the now numbered list into a 3 layer decoded list
    decoded_list = []
    for trans_num1 in trans_askii_list:
        try:
            decoded_list.append(trans_num1 - user_num)
        except:
            decoded_list.append(trans_num1)
### this will turn the encoded list back into a string of leters
    alphabet_dict_reverused = {value: key for key, value in alphabet_dict.items()}
    decoded_string = ""
    for decoded_num in decoded_list:
        try:
            if decoded_num > 26:
                while decoded_num > 26:
                    if decoded_num - 26 < 1:
                        decoded_num -= 25
                    else:
                        decoded_num -= 26
            decoded_string += alphabet_dict_reverused[decoded_num]
        except:
            decoded_string += str(decoded_num)
    return decoded_string
print(CeasarDecoder("hello world",5))