print("Welcome to the love calculator!")
name1 = input("What is your name?\n")
name2 = input("What is your name?\n")

# Convert both names to lowercase
name1_lower = name1.lower()
name2_lower = name2.lower()

# Combine the names
name_combined = name1_lower + name2_lower

# Count occurrences of letters in "TRUE"
t = name_combined.count("t")
r = name_combined.count("r")
u = name_combined.count("u")
e = name_combined.count("e")
true = t + r + u + e

# Count occurrences of letters in "LOVE"
l = name_combined.count("l")
o = name_combined.count("o")
v = name_combined.count("v")
e = name_combined.count("e")
love = l + o + v + e

# Combine the counts to form the love score
love_score = int(str(true) + str(love))

# Check the love score and print the appropriate message
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
