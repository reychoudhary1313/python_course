def count_vowels(word):
    vowels = ["a","e","i","o","u"]
    count = 0
    our_word = word.lower()
    for i in our_word:
        if i in vowels:
            count=count+1

    return count

result = count_vowels("Programming")
print(result)







