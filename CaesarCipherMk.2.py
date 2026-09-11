import random
def main():
    print("Wellcome to the Caesar Chipher Program")
    while True:
        program_input = input("1. Encoder\n2. Decoder\n0. Quit\n-> ")
        if program_input == "1":
            encode_input = input("1. type what you want to encode\n2. upload a file to encode\n-> ")
            if encode_input == "1":
                user_string = input("What do you want to encode?: ")
                try:
                    user_num = int(input("What do you want to shift by?: "))
                except:
                    user_num = 1
                print(encoder(user_string,user_num))
            elif encode_input == "2":
                while True:                        
                    if file_name == "q":
                        break
                    try:
                        file_name = input("What file do you want to encoded as a .txt or q to quit: ")
                        with open(file_name,"r") as fo:
                            encode_file = fo.read()
                            break
                    except:
                        continue
                    
                try:
                    user_num = int(input("What do you want to shift by?: "))
                except:
                    user_num = 1
                print(encode_file)
                print(encoder(encode_file,user_num))
        elif program_input == "2":
            user_string = input("What do you want to decode?: ")
            try:
                user_num = int(input("What do you want to shift by?: "))
            except:
                user_num = 1
            print(decoder(user_string,user_num))
        elif program_input == "0":
            break

def translation(string):
    alphabet_dict = {chr(i): i - 96 for i in range(97, 123)}
    trans_askii_list = []
    for let in string.lower():
        if let in alphabet_dict.keys():
            trans_askii_list.append(alphabet_dict[let])
        else:
            trans_askii_list.append(let)
    return trans_askii_list

def encoder(user_string,user_num = 1,):
    space_list = ["<",">","\\","|","~"]
    alphabet_dict = {chr(i): i - 96 for i in range(97, 123)}
    trans_askii_list = translation(user_string)
    encoded_list = []
    for trans_num in trans_askii_list:
        try:
            encoded_list.append(trans_num + user_num)
        except:
            encoded_list.append(trans_num)
    alphabet_dict_reverused = {value: key for key, value in alphabet_dict.items()}
    encoded_string = ""
    for encoded_num in encoded_list:
        try:
            if encoded_num == " ":
                random_index = space_list[random.randrange(len(space_list))]
                encoded_string += random_index
            elif encoded_num > 26:
                while encoded_num > 26:
                    encoded_num -= 26
                encoded_string += alphabet_dict_reverused[encoded_num]
        except:
            encoded_string += encoded_num
    return encoded_string


def decoder(user_string,user_num = 1,):
    space_list = ["<",">","\\","|","~"]
    alphabet_dict = {chr(i): i - 96 for i in range(97, 123)}
    trans_askii_list = translation(user_string)
    decoded_list = []
    for trans_num in trans_askii_list:
        try:
            decoded_list.append(trans_num - user_num)
        except:
            decoded_list.append(trans_num)
    alphabet_dict_reverused = {value: key for key, value in alphabet_dict.items()}
    decoded_string = ""
    for decoded_num in decoded_list:
        try:
            if decoded_num in space_list:
                decoded_string += " "
            elif decoded_num < 26:
                while decoded_num < 0:
                    decoded_num += 26
                decoded_string += alphabet_dict_reverused[decoded_num]
        except:
            decoded_string += decoded_num
    return decoded_string



print(encoder("something something",1))