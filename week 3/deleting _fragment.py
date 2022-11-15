s = input()
pos = s.find('h')
pos_2 = s.rfind('h')
print(s.replace(s[pos:pos_2 + 1], ''))
