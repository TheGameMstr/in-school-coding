from CaesarEnconder import CeasarEncoder; from CeasarDecoder import CeasarDecoder
print("Wellcome to the Caesar Cipher program!")
while True:
    user_input_screen = input("0. Encoder\n1. Decoder\nq. to quit\n-> ")
    if user_input_screen == "0":
        input_encoder = input("Type what you want to encode.\n-> ")
        num_encoder = int(input("How much do you want to shift by? leave blank for 1.\n-> "))
        print(CeasarEncoder(input_encoder, num_encoder))
    elif user_input_screen == "1":
        input_decoder = input("Type what you want to decode.\n->")
        num_decoder = int(input("What is the shift num?\n-> "))
        print(CeasarDecoder(input_decoder,num_decoder))
    elif user_input_screen == "q":
        break