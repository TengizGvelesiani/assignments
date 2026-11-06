import random

colors =["clubs", "diamonds", "hearts", "spades"]
val = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

print("Random card: " + random.choice(val) + " of " + random.choice(colors))