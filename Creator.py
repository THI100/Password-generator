def makePassword (SecurityLevel: str):
    print(f"MakePassword function called with security level: {SecurityLevel}")

    if SecurityLevel == "Lw":
        print("Low level selected")
    elif SecurityLevel == "Md":
        print("Medium level selected")
    elif SecurityLevel == "Hg":
        print("High level selected")
    elif SecurityLevel == "Ex":
        print("Extreme level selected")
    else:
        print("Error: Invalid security level")