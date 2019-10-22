import math, os

# word sources
# http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/

def main():

    words = getWords("english_words.txt")
    tree = Tree("_", 0)

    for i in range(5):
        tally = getMap(words, i)
        addToTree(tree, tally)
        print(i)

    saveTree("distributions.txt", tree)

class Word:
    def __init__(self, word, frequency):
        self.word = word
        self.frequency = int(frequency)

class TallyDict:
    def __init__(self):
        self.dict = {}

    def increment(self, key, value = 1):
        if key in self.dict:
            self.dict[key] += value
        else:
            self.dict[key] = value

    def getSortedList(self):
        items = [(key, self.dict[key]) for key in self.dict]
        items.sort(key = lambda x: x[1], reverse = True)
        return items

    def __str__(self):

        items = [(key, self.dict[key]) for key in self.dict]
        items.sort(key = lambda x: x[1], reverse = True)

        lines = []
        for key, freq in items:
            lines.append(key + hex(freq)[2:])

        return "\n".join(lines)

class Tree:
    def __init__(self, key, level):
        self.key = key
        self.letters = ""
        self.distribution = 1
        self.next = {}
        self.frequency = []
        self.level = level

    def add(self, key, letter, frequency):
        if key == "":
            self.letters += letter
            self.frequency += [frequency]
        else:
            if key[0] not in self.next:
                self.next[key[0]] = Tree(key[0], self.level + 1)
            self.next[key[0]].add(key[1:], letter, frequency)

    def normalize(self):
        pairs = [(self.letters[i], self.frequency[i]) for i in range(len(self.letters))]
        pairs.sort(key = lambda x: x[1], reverse = True)
        self.letters = ''.join([p[0] for p in pairs])
        self.frequency = [p[1] for p in pairs]

        fc = len(self.frequency)
        self.frequency = [i / self.frequency[0] for i in self.frequency]

        if fc <= 1:
            self.distribution = 1
        else:
            squaredError = sum([(self.frequency[i] - (1-i/(fc-1)))**2 for i in range(fc)])
            for p in range(2, 100):
                se = sum([(self.frequency[i] - (1-i/(fc-1))**p)**2 for i in range(fc)])
                if se < squaredError:
                    squaredError = se
                else:
                    self.distribution = p-1
                    break

    def __str__(self):
        self.normalize()

        indent = "  " * self.level
        strings = [indent + self.key + str(len(self.next)).zfill(2) + str(self.distribution).zfill(2) + self.letters]

        for n in self.next:
            strings.append(str(self.next[n]))

        return '\n'.join(strings)


def getInitialMap(words):

    tally = TallyDict()

    for word in words:
        letter = word.word[0]
        tally.increment(letter, transformedFrequency(word.frequency))

    return tally

def getMap(words, keyLength):

    tallyDict = TallyDict()

    for word in words:
        w = word.word
        if len(w) >= keyLength + 1:
            for i in range(len(w) - keyLength):
                key = w[i:i+keyLength+1]
                tallyDict.increment(key, transformedFrequency(word.frequency))

    return tallyDict

def transformedFrequency(frequency):
    # return math.ceil(math.log10(frequency))
    return frequency
    # return frequency ** 2
    # return 1

def addToTree(tree, tallyDict):
    for string, frequency in tallyDict.getSortedList():
        key = string[:-1]
        letter = string[-1]
        tree.add(key, letter, frequency)

def saveTree(filename, tree):
    
    with open(filename, "w") as file:
        file.write(str(tree))

    print("saved " + filename)

def saveList(filename, tallyDict):

    with open(filename, "w") as file:
        file.write(str(tallyDict))

    print("saved " + filename)

def getWords(filename):

    words = []
    lines = []
    
    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.split()
        words.append(Word(line[0], line[1]))

    return words

if __name__ == "__main__":
    main()