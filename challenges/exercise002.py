# Create a list comprehension that extracts all words from a list of sentences
# that are longer than 4 characters and converts them to uppercase.

sentences = [
    "Python is amazing",
    "List comprehensions are powerful",
    "Code with style",
    "Keep it simple"
]

# Write your list comprehension here:
#long_words = [sentence for sentence in sentences.split() if len(sentence) > 4]
words = [word.upper() for sentence in sentences for word in sentence.split() if len(word) > 4]
print(words)
# Convert to uppercase
# uppercase_words = [word.upper() for word in words]
# print(uppercase_words)
# Expected results: ['PYTHON', 'AMAZING', 'COMPREHENSIONS', 'POWERFUL', 'SIMPLE']