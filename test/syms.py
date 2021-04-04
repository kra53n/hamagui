txt = "[parse it] and [parse it too]"
print(len(txt))
pos = 0
poss = []
sym1 = "["
sym2 = "]"
print(txt)
sym = sym1
while len(txt) > pos:
    if txt[pos] == sym1 or txt[pos] == sym2:
        poss.append(pos)
    pos += 1
for i in range(0, len(poss), 2):
    print(txt[poss[i]+1:poss[i+1]])
