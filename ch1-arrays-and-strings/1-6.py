# 1.6	String Compression
#
# Write a function that converts strings into a simple compressed representation
# ex. 	ab 		-> a1b1
# 		aab 	-> a2b1
# 		cbbbc 	-> c1b3c1

def compress(string):
	counts = []
	count_index = 0
	for i in range(len(string)):
		if i == 0:
			counts.append([string[i],1])
		elif string[i-1] != string[i]:
			counts.append([string[i],1])
			count_index += 1
		else:
			counts[count_index][1] += 1

	return "".join(["".join(str(item)) for lst in counts for item in lst])

print(compress(input()))
