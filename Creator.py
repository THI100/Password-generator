import random

def makePassword (SecLVL: str, type_: str):
    print(f"MakePassword function called with security level: {SecLVL}, type: {type_}")

    Password = ""

    if type_ == "Alphanumeric":
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        SAFEind = round(len(characters) / 2)
        ind = len(characters) - 1

        if SecLVL == "Lw":
            RndIndex = random.randint(0, ind)
            for i in range(8):
                Password += characters[RndIndex + i % len(characters)]

        elif SecLVL == "Md":
            for i in range(8):
                RndIndex = random.randint(0, ind)
                Password += characters[RndIndex]

        elif SecLVL == "Hg":
            for i in range(6):
                RndIndex = random.randint(0, ind)
                Password += characters[RndIndex]
            for i in range(4):
                RNDINDEx = random.randint(SAFEind, ind)
                Password += characters[RNDINDEx]
            for i in range(2):
                RndIndex = random.randint(0, ind)
                Password += characters[RndIndex]

        elif SecLVL == "Ex":
            for i in range(3):
                RndIndex = random.randint(0, ind)
                Password += characters[RndIndex]
            for i in range(2):
                RNDINDEx = random.randint(SAFEind, ind)
                Password += characters[RNDINDEx]
            for i in range(4):
                RndIndex = random.randint(0, ind)
                Password += characters[RndIndex]
            for i in range(3):
                RNDINDEx = random.randint(SAFEind, ind)
                Password += characters[RNDINDEx]

        else:
            print("Error: Invalid security level")

    elif type_ == "Numeric_4":
        characters = "0123456789"
        length = 4

        if SecLVL == "Lw":
            print("Low level selected")
        elif SecLVL == "Md":
            print("Medium level selected")
        elif SecLVL == "Hg":
            print("High level selected")
        elif SecLVL == "Ex":
            print("Extreme level selected")
        else:
            print("Error: Invalid security level")

    elif type_ == "Numeric_6":
        characters = "0123456789"
        length = 6

        if SecLVL == "Lw":
            print("Low level selected")
        elif SecLVL == "Md":
            print("Medium level selected")
        elif SecLVL == "Hg":
            print("High level selected")
        elif SecLVL == "Ex":
            print("Extreme level selected")
        else:
            print("Error: Invalid security level")

    elif type_ == "ASCII":
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:',.<>?/"
        length = 12

        if SecLVL == "Lw":
            print("Low level selected")
        elif SecLVL == "Md":
            print("Medium level selected")
        elif SecLVL == "Hg":
            print("High level selected")
        elif SecLVL == "Ex":
            print("Extreme level selected")
        else:
            print("Error: Invalid security level")

    else:
        print("Error: Invalid password type")
        return
    
    print(f"Generated password: {Password}")