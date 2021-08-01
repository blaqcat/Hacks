import string


def encrypt(text, shift):
    encrypted_text = list(range(len(text)))
    alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    shifted_alphabet = second_half + first_half

    for i, letter in enumerate(text.lower()):

        if letter in alphabet:
            original_index = alphabet.index(letter)
            new_letter = shifted_alphabet[original_index]
            encrypted_text[i] = new_letter
        else:
            encrypted_text[i] = letter

    return "".join(encrypted_text)


def decrypt(text, shift):
    """ when the shift is known """
    decrypted_text = list(range(len(text)))
    alphabet = string.ascii_lowercase
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    shifted_alphabet = second_half + first_half

    for i, letter in enumerate(text.lower()):

        if letter in alphabet:
            index = shifted_alphabet.index(letter)
            original_letter = alphabet[index]
            decrypted_text[i] = original_letter
        else:
            decrypted_text[i] = letter

    return "".join(decrypted_text)


def brute_force_decrypt(text):
    """ when the shift is unknown """
    for n in range(26):
        print(f"Using a shift value of {n}")
        print(decrypt(text, n))
        print("\n***\n")


e = encrypt("how now brown cow", 8)
# 'pwe vwe jzwev kwe'
print(decrypt(e, 8))
# 'how now brown cow'
brute_force_decrypt(e)