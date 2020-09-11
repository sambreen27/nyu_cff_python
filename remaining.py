#Name: Saba Ambreen
#Lesson 7.3: Remaining Words Function

words = "the quick brown fox"

def remainingwords(words):
    remained_words = words.split()[1:]
    convert_to_string = ' '.join(remained_words)
    return convert_to_string
    
remainingwords(words)
