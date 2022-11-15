s = input()
pos = s.find('f')
pos_2 = s.rfind('f')
if pos >= pos_2 and pos != -1:
    print(pos)
elif pos + pos_2 > -1:
    print(pos, pos_2)
