
#count syllables
def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

all_words_list=[]
words_list=[]
syllables_total=0
i=0
#enter words 


while True:
    word=input("Enter a word:")
    if word=="END":
        break
    if syllable_count(word)<=7:
        all_words_list.append(word)
    else:
        print("Word is too long-should be less than 8 syllables")
print(all_words_list)
#select words
while syllables_total<17 or not words_list:
    word=all_words_list[0]
    
    if syllable_count(word)<=7:
        if syllable_count(word)>5:
            if len(max(words_list, key=len))>5:
                print("Only one word with more than 5 syllables")
            else:
                syllables_total=syllables_total+syllable_count(word)
                if syllables_total<17:
                    words_list.append(word)
                    words_list.pop(0)
                else:
                    syllables_total=syllables_total-syllable_count(word)
        else:
            syllables_total=syllables_total+syllable_count(word)
            if syllables_total<17:
                words_list.append(word)
                words_list.pop(0)
            else:
                syllables_total=syllables_total-syllable_count(word)
    i=i+1
    print(all_words_list)
#create haiku

print(words_list)

# wordwordwordwordwordwordwordword

