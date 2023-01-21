import hashlib
import pyfiglet

def doozy():
    ascii_art = pyfiglet.figlet_format("doozy")
    print(ascii_art)

doozy()

def crack_password(password_hash, wordlist):
    """
    Cracks a password hash using a wordlist.
    """
    with open(wordlist, "r") as f:
        for line in f:
            word = line.strip()
            hash_word = hashlib.md5(word.encode()).hexdigest()
            if hash_word == password_hash:
                return word
    return None

password_hash = input("Enter the password hash: ")
wordlist = input("Enter the path to the wordlist file: ")
cracked_password = crack_password(password_hash, wordlist)
if cracked_password:
    print("Password found:", cracked_password)
else:
    print("Password not found in wordlist.")
