def makePassword (SecLVL: str, type_: str):
    print(f"MakePassword function called with security level: {SecLVL}, type: {type_}")

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