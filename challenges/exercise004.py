# Create a list comprehension that processes a list of text strings and extracts only those
# strings where the word count is greater than 3, returning the word count for each qualifying string.
# Use the walrus operator to avoid calculating the word count twice.

texts = [
    "Hello world",
    "Python programming is fun and powerful",
    "AI",
    "List comprehensions make code concise",
    "Short text",
    "Machine learning algorithms are complex but fascinating",
    "Code"
]

# Write your list comprehension here using the walrus operator:
#word_counts = 
# goes through texts list and sets word as each comma. Word = result so its for word in texts
word1=[word for word in texts]
# starts with for sentence in text goes through each string in texts, like the above output
# then for word in sentence.splint goes through each sentence, splits it into individual words and goes through each word
words =[ word for sentence in texts for word in sentence.split()]
print (words)
# Now, filter the words to only include those with more than 3 characters and get their lengths
word_counts = [len(word) for word in words if len(word) > 3]
print(word_counts)
sentences = [sentence for sentence in texts if len(sentence.split()) > 3]
print(sentences)
Answer = [len(sentence.split()) for sentence in sentences]
print(Answer)
# Expected results: [6, 5, 7]