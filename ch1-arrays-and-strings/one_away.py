# one_away.py

# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character. Write
# a function to check whether two strings are one edit apart.

def one_added(a, b):
    longer = a
    shorter = b
    deletions = 0;

    if len(a) < len(b):
        longer = b
        shorter = a

    for i in range(len(longer)):
        deletions = i
        if longer[i] != shorter[i-deletions]:
            deletions += 1;

    return deletions == 1

def one_replaced(a, b):
    diffs = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            diffs += 1
            if diffs > 1:
                return False

    return True

def one_away(a, b):
    if abs(len(a)-len(b)) > 1:
        return False
    elif abs(len(a)-len(b)) == 1:
        return one_added(a, b)
    else:
        return one_replaced(a, b)

a = input()
b = input()

print(one_away(a, b))
