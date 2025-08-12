import random

def generate_from_pattern(characters, pattern, safe_index=None):
    """Generate a password given a list of (count, range_type) tuples."""
    result = ""
    length = len(characters) - 1
    for count, mode in pattern:
        for _ in range(count):
            if mode == "any":
                idx = random.randint(0, length)
            elif mode == "safe":
                idx = random.randint(safe_index, length)
            elif mode == "seq":  # sequential from random start
                start = random.randint(0, length)
                idx = (start + _) % len(characters)
            elif mode == "mul":  # multiply index by position
                start = random.randint(0, length)
                idx = (start * _ % len(characters))
            result += characters[idx]
    return result

def makePassword(SecLVL: str, type_: str):
    print(f"MakePassword called with: SecLVL={SecLVL}, type={type_}")

    charsets = {
        "Alphanumeric": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "Numeric_4": "0123456789",
        "Numeric_6": "0123456789",
        "ASCII": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:',.<>?/"
    }

    lengths = {
        "Alphanumeric": 8,
        "Numeric_4": 4,
        "Numeric_6": 6,
        "ASCII": 8
    }

    if type_ not in charsets:
        print("Error: Invalid password type")
        return

    characters = charsets[type_]
    safe_index = round((len(characters) - 1) / 2)

    # Define patterns for each security level
    patterns = {
        "Lw": [(lengths[type_], "seq")],
        "Md": [(lengths[type_], "any")],
        "Hg": [(6, "any"), (4, "safe"), (2, "any")] if lengths[type_] == 8 else [(lengths[type_], "seq")],
        "Ex": [(3, "any"), (2, "safe"), (4, "any"), (3, "safe")] if lengths[type_] == 8 else [(lengths[type_], "mul")]
    }

    if SecLVL not in patterns:
        print("Error: Invalid security level")
        return

    password = generate_from_pattern(characters, patterns[SecLVL], safe_index)
    print(f"Generated password: {password}")