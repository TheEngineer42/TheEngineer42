x = input("write text to cipher ")

encrypted_text = ""

for char in x:
    if 'a' <= char <= 'z':
        encrypted_char = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
        encrypted_text += encrypted_char
    else:
        encrypted_text += char

print("ciphered text:", encrypted_text)
