from CIPHER_ART import logo
print(logo)   
import getpass
def restart(r):
    if r=="yes":
        loop()
    elif r=="no":
        pass
    else:
        print("Type right input")
        r=input("Type 'YES' if you want to start again,otherwise type 'NO'\n").lower()
        
def encrypt():
    message=getpass.getpass("Type the message\n").lower()
    gear=int(getpass.getpass("Enter the shift\n"))
    if gear> 15:
        gear=round(gear/5)
    c=""
    for j in message:
        if j .isalpha():
            p=alphabets.index(j)
            s=round(p+gear)
            if s>25:
                s-=26
            c+=(alphabets[s])
        elif j.isnumeric():
            p=numbers.index(j)
            s=round(p+gear)
            if s>9:
                s-=10
            c+=(numbers[s])
        else:
            p=symbols.index(j)
            s=round(p+gear)
            if s>(len(symbols)-1):
                s-=len(symbols)
            c+=(symbols[s])
    print(f"The encrpyted code is '{c}'")
    
def decrypt():
    message=getpass.getpass("Type the message\n").lower()
    gear=int(getpass.getpass("Enter the shift\n"))
    if gear>15:
        gear=round(gear/5)
    c=""
    for j in message:
        if j .isalpha():
            p=alphabets.index(j)
            s=round(p-gear)
            c+=(alphabets[s])
        elif j.isnumeric():
            p=numbers.index(j)
            s=round(p-gear)
            c+=(numbers[s])
        else:
            p=symbols.index(j)
            s=round(p-gear)
            c+=(symbols[s])
    print(f"The decrypted code is '{c}'")
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'," "]
def loop():
    intro=True
    while  intro:
        method=input("Type 'Encode' to encode, Type 'Decode' to Decode\n").lower()
        if method=="encode":
            encrypt()
            r=input("Type 'YES' if you want to start again,otherwise type 'NO'\n").lower()
            restart(r)
            intro=False
        elif method=="decode":
            decrypt()
            r=input("Type 'YES' if you want to start again,otherwise type 'NO'\n").lower()
            restart(r)
            intro=False
        else: 
            print("Enter the right method")
loop()