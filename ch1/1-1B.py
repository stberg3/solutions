# 1.1B Determine if a string has all unique characters (no addn' data structures)

def all_unique(word):
    for i in range(len(word)):
        for j in range(i+1,len(word)):
            if word[i] == word[j]:
                return False
    return True

print(all_unique(input()))
