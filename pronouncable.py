import sys, random

def main():

    tree = initTree("distributions.txt")

    length = int(sys.argv[1])
    count = int(sys.argv[2])
    for i in range(count):
        string = ""
        for j in range(length):
            string += genNext(tree, string)
        print(string.lower())
        
class Tree:
    def __init__(self, key, distribution, letters):
        self.key = key
        self.letters = letters
        self.distribution = distribution
        self.next = {}

    def add(self, tree):
        self.next[tree.key] = tree

    def get(self, key):
        
        if key == "":
            return self.letters, self.distribution
        else:
            n = key[0]
            if n in self.next:
                return self.next[n].get(key[1:])
            else:
                return None, None

def initTree(filename):

    with open(filename) as file:
        content = file.readlines()

    rootLine = content[0]
    key = rootLine[0]
    childCount = int(rootLine[1:3])
    distribution = int(rootLine[3:5])
    letters = rootLine[5:].strip()

    root = Tree("", distribution, letters)

    treeStack = [root]
    countStack = [childCount]
    
    for line in content[1:]:

        line = line.strip()
        key = line[0]
        childCount = int(line[1:3])
        distribution = int(line[3:5])
        letters = line[5:].strip()
        child = Tree(key, distribution, letters)

        while countStack[-1] == 0:
            treeStack.pop()
            countStack.pop()
        
        countStack[-1] -= 1

        treeStack[-1].add(child)
        treeStack.append(child)
        countStack.append(childCount)

    return root

def genNext(tree, string):

    r = random.random()

    key = string[-4:]
    l, d = None, None

    while l == None:
        l, d = tree.get(key)
        key = key[1:]

    i = int((1 - pow(r, 1/d)) * len(l))

    # print(l, d, r, i)

    return l[i]

if __name__ == "__main__":
    main()