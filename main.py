from itertools import product

# Define the characters and placement size
characters = ['1', '2', '3', '4']
placement_size = 5

# Generate all possible combinations and write to file
with open("results.txt", "w") as f:
    for p in product(characters, repeat=placement_size):
        f.write(''.join(p) + "\n")
        # you can give your own custom instruction right here
