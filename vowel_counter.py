# Program to count vowel occurrences in a sentence

sentence = input("Enter a sentence: ").lower()  # convert to lowercase for easy checking

vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

# Count each vowel
for char in sentence:
    if char in vowels:
        vowels[char] += 1

# Print results
print("\nVowel Count:")
for vowel, count in vowels.items():
    print(f"{vowel}: {count}")
