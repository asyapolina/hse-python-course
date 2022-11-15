z = int(input())
x = int(input())
y = int(input())
a = x * 100 + y
p = a / 100 * z
print(int((a + p) // 100), int((a+p) % 100))
