# 1.1 Determine if a string has all unique characters

def all_unique(word):
    char_set = set(word)
    return len(char_set) == len(word)

print(all_unique(input())) 
