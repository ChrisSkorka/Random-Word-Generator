import math

"""
Reorder the words by their 'pronouncability' score as determined by the previous pronouncability distribution model
"""

initial = {}
first   = {}
second  = {}
third   = {}
forth   = {}
fifth   = {}

def main():
    global initial, first, second, third, forth, fifth
    
    folder = "data-f"

    initial = initDicts(folder+"/tally0.txt", 0)
    first   = initDicts(folder+"/tally1.txt", 0)
    second  = initDicts(folder+"/tally2.txt", 1)
    third   = initDicts(folder+"/tally3.txt", 2)
    forth   = initDicts(folder+"/tally4.txt", 3)
    fifth   = initDicts(folder+"/tally5.txt", 4)

    words = getWords("english_words.txt")

    for word in words:
        w = word.word
        p = getPronouncability(w) * math.log(word.frequency) * math.log(len(word.word))
        word.pronouncability = p

    words.sort(key = lambda w:w.pronouncability, reverse = True)
    saveWords("words/words-freq-filtered.txt", words)

class Word:
    def __init__(self, word, frequency):
        self.word = word
        self.frequency = int(frequency)
        self.pronouncability = 0

def getWords(filename):

    words = []
    lines = []
    
    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.split()
        words.append(Word(line[0], line[1]))

    print("done " + filename)

    return words

def saveWords(filename, words):
    string = ""

    for word in words:
        # string += word.word + " " + str(word.pronouncability) + "\n"
        string += word.word + " " + str(word.frequency) + "\n"
        # string += word.word + "\n"

    with open(filename, "w") as file:
        file.write(string)

    print("saved " + filename)

class LetterDict:
    def __init__(self):
        self.len = 0
        self.frequencySum = 0
        self.letters = {}

    def add(self, letter, frequency):
        self.len += 1
        self.frequencySum += frequency
        self.letters[letter] = frequency

    def getLiklyhood(self, letter):
        if letter in self.letters:
            return self.letters[letter] / self.frequencySum
        else:
            return 0

def initDicts(filename, keyLength):

    with open(filename) as file:
        content = file.readlines()

    dictionary = {}

    for line in content:

        key = line[:keyLength]
        letter = line[keyLength]
        frequency = line[keyLength+1:]
        if key not in dictionary:
            dictionary[key] = LetterDict()
        dictionary[key].add(letter, int(frequency, 16))
        
    print("done " + filename)
            
    return dictionary

def getPronouncability(word):

    liklyhoodSum = 0

    for i in range(1, len(word)):
        liklyhoodSum += getLiklyhoodOfLastLetter(word[:i+1])

    return 0 if len(word) <= 1 else liklyhoodSum / (len(word) - 1)

def getLiklyhoodOfLastLetter(string):
    global initial, first, second, third, forth, fifth

    letter = string[-1]
    key1 = string[-2:-1]
    key2 = string[-3:-1]
    key3 = string[-4:-1]
    key4 = string[-5:-1]

    if len(key4) == 4 and key4 in fifth:
        return fifth[key4].getLiklyhood(letter)
    if len(key3) == 3 and key3 in forth:
        return forth[key3].getLiklyhood(letter)
    if len(key2) == 2 and key2 in third:
        return third[key2].getLiklyhood(letter)
    if len(key1) == 1 and key1 in second:
        return second[key1].getLiklyhood(letter)

    print("strange at getLiklyhoodOfLastLetter ")
    return 0

if __name__ == "__main__":
    main()