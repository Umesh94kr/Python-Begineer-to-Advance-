alphabets = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

def encode(text, position):
    new_text = ""
    for char in text:
        if char in alphabets:
            idx = alphabets.index(char)
            if idx + position >= 26:
                idx = idx + position - 26
                new_text += alphabets[idx]
            else:
                new_text += alphabets[idx + position]
        else:
            new_text += char
    return new_text

def decode(text, position):
    new_text = ""
    for char in text:
        if char in alphabets:
            idx = alphabets.index(char)
            if idx - position < 0:
                new_text += alphabets[idx - position]
            else:
                new_text += alphabets[idx - position]
        else:
            new_text += char
    return new_text


print("Welcome to Cesae Cypher!")

start = True
while(start):
    decode_or_encode = input("Do you want to decode or encode? ")
    if decode_or_encode == 'decode':
        text = input("Enter the text to decode - ")
        position = int(input("By how much you want to shift forward? "))
        encoded_text = encode(text, position)
        print(f"Encoded text : {encoded_text}")
    elif decode_or_encode == 'encode':
        text = input("Enter the text to encode - ")
        position = int(input("By how much you want to shift backward? "))
        decoded_text = decode(text, position)
        print(f"Decoded text : {decoded_text}")

    to_continue = input("Do you want to continue further? Yes or No")
    if to_continue == 'Yes':
        start = True 
    else:
        start = False

    