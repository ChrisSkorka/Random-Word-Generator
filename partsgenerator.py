from sys import stdin

import random

class alphabet:

	def __init__(self):
		self.letters = dict()
		
class table:
	
	def __init__(self):
		self.dictionary = dict()

def tally(length, word, dictionary):

	for i in range(len(word)-length+1):
		substring = word[i:i+length-1]
		last = word[i+length-1]
		
		if substring not in dictionary:
			dictionary[substring] = alphabet()
			
		if last not in dictionary[substring].letters:
			dictionary[substring].letters[last] = 0
			
		dictionary[substring].letters[last] += 1

def sortedList(dictionary):

	return sorted(dictionary.items(), key = lambda dictionary: dictionary[1], reverse=True)

def main():

	alphabet1 = alphabet()
	dictionary = dict()
	
	for line in stdin:
		line = line.split()
		
		frequency = int(line[1])
		word = line[0]
		
		for l in word:
		
			if l not in alphabet1.letters:
				alphabet1.letters[l] = 0
				
			alphabet1.letters[l] += 1
		
		#tally(5, word, dictionary)

	for tuple in sortedList(alphabet1.letters):
		print("_", tuple[0], tuple[1])
		
	#for substring in dictionary:
	#	for tuple in sortedList(dictionary[substring].letters):
	#		print(substring, tuple[0], tuple[1])
	
	#for substring in table3.dictionary:
	#	for letter in table3.dictionary[substring].letters:
	#		print(substring, letter, table3.dictionary[substring].letters[letter])
		
	
	#print(sortedList(dictionary1))
	#print(sortedList(dictionary2))
	#print(sortedList(dictionary3))
	#print(sortedList(dictionary4))
	
if __name__ == "__main__":
	main()