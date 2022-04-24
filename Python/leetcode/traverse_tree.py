import itertools

def reverseWordsInString(string):
    # Write your code here.
	# get 2 list and 1 flag, 2 lists contain words
	if not string:
		return string
	whitespace_set = {"\t", " ", "\n"}
	whitespace_first = string[0] in whitespace_set
	curr = ""
	getting_whitespace = whitespace_first
	whitespaces = []
	words = []
	curr = string[0]
	for c in string[1:]:
		if getting_whitespace and c in whitespace_set:
			curr += c
		elif getting_whitespace and c not in whitespace_set:
			whitespaces.append(curr)
			curr = c
			getting_whitespace = False
		elif not getting_whitespace and c in whitespace_set:
			words.append(curr)
			curr = c
			getting_whitespace = True
		else:
			curr += c
	if getting_whitespace:
		whitespaces.append(curr)
	else:
		words.append(curr)

	words = words[::-1]
	whitespaces = whitespaces[::-1]
	components = list(itertools.zip_longest(whitespaces, words))
	components = list(itertools.chain.from_iterable(components))
	components = [c for c in components if c is not None]
    return "".join(components)



if __name__ == "__main__":
    print(underscorifySubstring("abcabcabcabcabc", "abc"))
