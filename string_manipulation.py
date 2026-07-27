sentence = input("Enter a sentence:")

uppercase_sentence = sentence.upper()
print("Uppercase:", uppercase_sentence)

reversed_sentence = sentence[::-1]
print("Reversed:", reversed_sentence)

vowels = "aeiou"
count = 0

for char in sentence.lower():
    if char in vowels:
        count += 1

print("Vowel Count:", count)

hyphenated_sentence = sentence.replace(" ", "-")
print("Hyphenated:", hyphenated_sentence)
