def count_vowels(text):

    count=0
    for character in text.lower():
        if character in "aeiou":
            count+=1

    return count

    





result=count_vowels("sadia")
print("number of vowels:",result)