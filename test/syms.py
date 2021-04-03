def __get_from_text_between_symbols(text, sym1, sym2):
    """
    Parse text from string between two symbols
    """
    inf = []
    pos1, pos2 = 0, 0
    while len(text) != pos1:
        while (text[pos1] != sym1) and (len(text)-1 > pos1):
            pos1 += 1
            print(len(text), pos1)
        while (text[pos2] != sym2) and (len(text)-1 > pos2):
            pos2 += 1
            inf.append(text[pos1+1:pos2])
        print(inf)
        input()
        pos1 += 1
        pos2 += 1
    return inf
print(__get_from_text_between_symbols("[sdifjbsadlfj], [dfigbldsjbng]", "[", "]"))
