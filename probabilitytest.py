import random

p = 5
c = 10

expected = [(i/(c-1))**p for i in range(c)]

tally = [1 for i in range(c)]

for i in range(100000):
    r = random.random()
    d = int(r**(1/p) * c)
    tally[d] += 1

results = [i / tally[-1] for i in tally]

print("expected")
for i in expected:
    n = round(i * 50)
    print(str(round(i, 4)).zfill(6), ' ', "█"*n)
    
print("results")
for i in results:
    n = round(i * 50)
    print(str(round(i, 4)).zfill(6), ' ', "█"*n)