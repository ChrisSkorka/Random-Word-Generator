from sys import stdin
import random

dictionary = []

frequecyCount = 0

for line in stdin:
	line = line.split()
	word_frequency = [line[0], int(line[1])]
	
	if len(word_frequency[0]) > 5 or True:
	
		frequecyCount += word_frequency[1]
		
		dictionary.append(word_frequency)
	
#print(dictionary)
	
combination = ""
for _ in range(3):
	randomNumber = random.randint(0, frequecyCount-1)
	
	
	for word_frequency in dictionary:
		randomNumber -= word_frequency[1]
		
		if randomNumber < 0:
			
			combination += word_frequency[0]
			break
			
print(combination)