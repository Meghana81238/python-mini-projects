alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position+shift_key)%26
            cipher_text+=alphabets[new_position] 
        else:
            cipher_text+=char
    print(f"here's the encrypted result:{cipher_text}")

def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position-shift_key)%26
            plain_text+=alphabets[new_position] 
        else:
            plain_text+=char
    print(f"here's the decrypted result:{plain_text}")


wanna_end=False
while not wanna_end:
    what_to_do=input("type 'encrypt' for encryption, type 'decrept' for decryption: ").lower()
    text=input("type your message:").lower()
    shift=int(input("type the shift number:"))
    if what_to_do=="encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=="decript":
        decryption(cipher_text=text,shift_key=shift) 
    play_again=input("type yes if you want to continue... otherwise type no.").lower() 
    if play_again=="no":
        wanna_end=True   
