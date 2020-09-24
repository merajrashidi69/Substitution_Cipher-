#keyboard_cipher
e_d = None
decrypted_text = {'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p', 'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g', 'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z', 'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n', 'z': 'm'}
encrypted_text = {'q': 'a', 'w': 'b', 'e': 'c', 'r': 'd', 't': 'e', 'y': 'f', 'u': 'g', 'i': 'h', 'o': 'i', 'p': 'j', 'a': 'k', 's': 'l', 'd': 'm', 'f': 'n', 'g': 'o', 'h': 'p', 'j': 'q', 'k': 'r', 'l': 's', 'z': 't', 'x': 'u', 'c': 'v', 'v': 'w', 'b': 'x', 'n': 'y', 'm': 'z'}


def shifted(password):
    password = password.lower()
    result = ""
    for x in password:
        for i in x:
            if i != ' ':
                result = result + e_d[i]
            else:
                result = result + ' '
    return result


def main():
    global e_d
    enc_or_dec = input('Do you want to (c)ipher or (d)ecipher? ')
    if enc_or_dec == 'c':
        e_d = dict(encrypted_text)
    else:
        e_d = dict(decrypted_text)
    password = input('Enter the secret password: ')
    result = shifted(password)
    print(result)

while True:
    main()

