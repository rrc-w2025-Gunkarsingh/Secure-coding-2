# little_big_bad_python.py
import random
import time

print("🐍 Welcome to Little Big Bad Python!")
time.sleep(1)

size = random.randint(1, 10)

print(f"\nA python appears... It looks size level {size}!")

action = input("\nDo you (r)un or (f)ight? ").lower()

if action == "r":
    if size > 5:
        print("\nYou barely escape! That was a BIG bad python! 😰")
    else:
        print("\nIt was tiny... you ran from THAT? 😂")
elif action == "f":
    if size <= 5:
        print("\nYou bravely defeat the little python! 🏆")
    else:
        print("\nOh no... it was BIG and BAD! Game over 💀")
else:
    print("\nThe python is confused. You both stare awkwardly. 👀")

print("\nThanks for playing!")
