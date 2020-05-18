a= ["yo","act","flop","tac","cat","oy","olfp"]

#output = [["yo","oy"],["act","tac","cat"],["flop","olfp"]]

def groupAnagrams(string):
	anagrams = {}
	for sub in string:
		sortedWord = "".join(sorted(sub))
		if sortedWord in anagrams:
			anagrams[sortedWord].append(sub)
		else:
			anagrams[sortedWord] = [sub]
	return list(anagrams.values())

ans = groupAnagrams(a)
print(ans)