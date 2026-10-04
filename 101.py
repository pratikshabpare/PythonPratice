text="python programming"
count=0
consonants=0
for ch in text:
    if ch in "aeiou":
        count +=1
    elif ch.isalpha():
        consonants +=1
print(count)
print(consonants)