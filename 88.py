sentence="Python is easy to learn"
words=sentence.split()
# count=len(words)
# print(count)
largest=""
for word in sentence:
    if len(word) > len (largest):
        largest=word
print(largest)