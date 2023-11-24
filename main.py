import random
import base64
import hashlib
import codecs
import os
from colorama import *

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()
print(f"\n{Fore.CYAN}[INFO]{Fore.RESET} Password generator\n")
print("1. Random password\n2. Hashed\n")
user_option = input(f"{Fore.YELLOW}[!]{Fore.RESET} :$: ")

if user_option == "1":
    count = int(input(f"{Fore.YELLOW}[!]{Fore.RESET} Amount: "))
    print(f"\n{Fore.CYAN}[INFO]{Fore.RESET} Random password\n")
    for i in range(count):
        lower_letters = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        upper_letters = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
        characters = "!", "£", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", "@", "#", "~", ",", "<", ".", ">", "/", "?"
        print(f"{Fore.YELLOW}[!]{Fore.RESET} Password: {random.choice(characters)}{random.choice(upper_letters)}{random.choice(characters)}{random.choice(upper_letters)}{random.choice(lower_letters)}{random.choice(characters)}{random.choice(upper_letters)}{random.choice(lower_letters)}{random.choice(upper_letters)}{random.choice(upper_letters)}{random.choice(lower_letters)}{random.choice(upper_letters)}{random.choice(lower_letters)}{random.choice(characters)}{random.choice(upper_letters)}{random.choice(lower_letters)}{random.choice(upper_letters)}{random.choice(characters)}{random.choice(upper_letters)}{random.choice(characters)}{random.choice(upper_letters)}{random.choice(lower_letters)}{random.choice(upper_letters)}{random.choice(characters)}{random.choice(upper_letters)}{random.choice(characters)}{random.choice(upper_letters)}{random.choice(lower_letters)}{random.choice(characters)}{random.choice(upper_letters)}{random.choice(lower_letters)}{random.choice(upper_letters)}{random.choice(characters)}{random.choice(upper_letters)}")

elif user_option == "2":
    count = int(input(f"{Fore.YELLOW}[!]{Fore.RESET} Amount: "))
    print(f"\n{Fore.CYAN}[INFO]{Fore.RESET} Hashed passwords")
    for i in range(count):



        lower_letters = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        upper_letters = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
        characters = "!", "£", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", "@", "#", "~", ",", "<", ".", ">", "/", "?"

        # Password generator
        password = f"{random.choice(upper_letters)}{random.choice(upper_letters)}{random.choice(lower_letters)}{random.choice(characters)}{random.choice(upper_letters)}{random.choice(lower_letters)}{random.choice(upper_letters)}{random.choice(upper_letters)}{random.choice(lower_letters)}{random.choice(upper_letters)}{random.choice(lower_letters)}{random.choice(characters)}{random.choice(upper_letters)}{random.choice(lower_letters)}{random.choice(upper_letters)}{random.choice(characters)}{random.choice(upper_letters)}{random.choice(characters)}{random.choice(upper_letters)}{random.choice(lower_letters)}{random.choice(upper_letters)}{random.choice(characters)}{random.choice(upper_letters)}{random.choice(characters)}{random.choice(upper_letters)}{random.choice(lower_letters)}{random.choice(characters)}{random.choice(upper_letters)}{random.choice(lower_letters)}{random.choice(upper_letters)}{random.choice(characters)}{random.choice(upper_letters)}"

        # SHA256 hasher
        sha256_hashed_data = hashlib.sha256(password.encode()).hexdigest()

        # MD5 hasher
        data_bytes = sha256_hashed_data.encode('utf-8')
        md5_hashed_data = hashlib.md5(data_bytes).hexdigest()  

        # Base64 encoder
        base64_bytes = md5_hashed_data.encode("ascii")
        base64_encoded_data = base64.b64encode(base64_bytes)

        # Rot13 encode
        rot13_encoded_data = codecs.encode(base64_encoded_data.decode("ascii"), 'rot_13')

        print(f"\n{Fore.YELLOW}[!]{Fore.RESET} Original password:", password)
        print(f"{Fore.YELLOW}[!]{Fore.RESET} SHA256 hashed password:", sha256_hashed_data)
        print(f"{Fore.YELLOW}[!]{Fore.RESET} MD5 hashed password:", md5_hashed_data)
        print(f"{Fore.YELLOW}[!]{Fore.RESET} Base64 encoded password:", base64_encoded_data)
        print(f"{Fore.YELLOW}[!]{Fore.RESET} Rot13 encoded password:", rot13_encoded_data)
        print(f"{Fore.YELLOW}[!]{Fore.RESET} Final password:", random.choice(upper_letters) + random.choice(lower_letters) + random.choice(characters) + rot13_encoded_data + random.choice(upper_letters) + random.choice(lower_letters) + random.choice(characters), end='\n')