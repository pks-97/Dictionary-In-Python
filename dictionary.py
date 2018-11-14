import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches


data = json.load(open("data.json"))


def correct(word):
	maxi = 0
	j = None
	for i in data:
		t = SequenceMatcher(None, word, i).ratio()
		if t > maxi:
			j = i
			maxi = t 
	return j		


def corr(word):
	return "Did you mean " + get_close_matches(word,data.keys(),1)[0] + " !"


def translate(word):
	w = word[0:1].upper() + word[1:len(word)]
	e = word.upper()
	# print(w)
	if word in data:
		print("There are " + str(len(data[word])) + " meanings of the word!")
		return data[word]
	elif w in data:
		print("There are " + str(len(data[w])) + " meanings of the word!")
		return data[w]
	elif e in data:
		print("There are " + str(len(data[e])) + " meanings of the word!")
		return data[e]
	elif len(get_close_matches(word,data.keys())) > 0:
		g = correct(word)
		# g = get_close_matches(word,data.keys())[0]
		yn =  input("Did you mean " + g + " ! ").lower()
		# print(g)
		if yn == "yes":
			print("There are " + str(len(data[g])) + " meanings of the word!")
			return data[g]
		elif yn == "no":
		    print("The word does not exist!")
		    return ""
		else:
		    print("We did not understand! ")  
		    return ""      
	else:
	    return "Please enter a valid word!"	


def tr(word):
	if word in data:
		return data[word]
	else:
	    return corr(word)	

# confirm = "yes"


word = str(input("Enter word:")).lower()
r = translate(word)
for i in range(0,len(r)):
	print(r[i] + "\n")
# print(translate(word))
# while confirm == "yes":
# 	word = (str(input("Enter word:"))).lower()
# 	if translate(word) == "Please enter a valid word!":

# print(tr(word))