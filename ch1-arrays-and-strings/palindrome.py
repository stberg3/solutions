# palindrome.py

# Make a program that says whether a given string is a permutation
# of a palindrome

from collections import defaultdict

def isPermPal(string):
    letter_counts = defaultdict(int)
    for c in string:
        letter_counts[c] += 1

    odds = 0
    for count in letter_counts.values():
        if count % 2 == 1:
            odds += 1

    if len(string) % 2 == 1:
        return odds < 2
    else:
        return odds == 0

string = input()
print(isPermPal(string))
