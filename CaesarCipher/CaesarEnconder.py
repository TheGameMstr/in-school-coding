def CeasarEncoder(string,user_num1 = 1):
    ### this turns leters into 1-26 useing ascii but trimed down for the 1-26 alphbet
    alphabet_dict = {chr(i): i - 96 for i in range(97, 123)}
    trans_askii_list = []
    for let in string.lower():
        if let in alphabet_dict.keys():
            trans_askii_list.append(alphabet_dict[let])
        else:
            trans_askii_list.append(let)
    ### this turns the now numbered list into a 3 layer encoded list but need tasnlated back
    encoded_list = []
    for trans_num1 in trans_askii_list:
        try:
            encoded_list.append(trans_num1 + user_num1)
        except:
            encoded_list.append(trans_num1)
    ### this will turn the encoded list back into a string of leters
    alphabet_dict_reverused = {value: key for key, value in alphabet_dict.items()}
    encoded_string = ""
    for encoded_num in encoded_list:
        try:
            if encoded_num > 26:
                while encoded_num > 26:
                    encoded_num -= 26
            encoded_string += alphabet_dict_reverused[encoded_num]
        except:
            encoded_string += encoded_num
    return encoded_string