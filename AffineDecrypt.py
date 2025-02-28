import string

def Nghich_Dao_modulo(a, m):
    a %= m
    for x in range (1, m):
        if (a * x) % m == 1:
            return x
    
    return None

def Decrypt_Affine(cipher_text, a, b):
    a_Nghich_Dao = Nghich_Dao_modulo(a, 26)
    if (a_Nghich_Dao is None) :
        return None
    
    Alphabets = string.ascii_uppercase
    Decrypt_Text = []
    
    for char in cipher_text:
        if (char.isupper()):
            y = ord(char) - ord('A')
            x = (a_Nghich_Dao * (y - b)) % 26
            Decrypt_Text.append(Alphabets[x])
        elif (char.islower()):
            y = ord(char.upper()) - ord('A')
            x = (a_Nghich_Dao * (y - b)) % 26
            Decrypt_Text.append(Alphabets[x].lower())
        else:
            Decrypt_Text.append(char)
    
    return ''.join(Decrypt_Text)

def Brute_Force(cipher_text):
    possible_a = [a for a in range(1, 26) if Nghich_Dao_modulo(a, 26) is not None]
    for a in possible_a:
        for b in range(26):
            decrypted_text = Decrypt_Affine(cipher_text, a, b)
            if decrypted_text:
                print(f"Trying a={a}, b={b}: {decrypted_text} \n")



if __name__ == "__main__":
    cipher_text = input("Nhap van ban bi ma hoa:")
    print("\nAttempting to decrypt using all possible keys:")
    Brute_Force(cipher_text)
    
        