from string import ascii_lowercase

# char to int
char2int = {x: idx for idx, x in enumerate(ascii_lowercase)}
# int to char
int2char = {idx: x for idx, x in enumerate(ascii_lowercase)}

def encrypt_shift(plain_text: str, k: int) -> str:
    """
    Shift for text 
    """
    plain_text = plain_text.replace(" ", "").lower()
    return "".join([int2char[(char2int[i] + k) % 26] for i in plain_text]).upper()


def decrypt_shift(cipher_text: str, k: int) -> str:
    
    cipher_text = cipher_text.replace(" ", "").lower()
    return "".join([int2char[(char2int[i] - k) % 26] for i in cipher_text])

if __name__ == "__main__":
    print(encrypt_shift("a",1))
