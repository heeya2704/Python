# Write a Python program to count the occurrences of each word in a given sentence. 

# Count occurrences of each word in a sentence

sentence = input("Enter sentence: ")

words = sentence.split()
freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

print(freq)