# 1-7 Rotate Matrix:
#
# Given an NxN matrix, where each element is 4 bytes, write a method to rotate
# the matrix by 90 degrees. Try to do the rotation in place.
#
# A A A       C B A
# B B B   ->  C B A
# C C C       C B A



def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j>i:
                continue
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    return matrix


test1 = [   ['A','A','A','A'],
            ['B','B','B','B'],
            ['C','C','C','C'],
            ['D','D','D','D']]

for row in test1:
    print(row)

print()
for row in rotate(test1):
    print(row)
