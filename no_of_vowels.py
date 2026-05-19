words = ["apple", "banana", "orange"]

vowels = "aeiou"

for word in words:

    count = 0

    for ch in word:

        if ch.lower() in vowels:
            count += 1

    print(word, "=", count, "vowels")