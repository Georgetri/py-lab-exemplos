num = int(input("Insira um número para saber a tabuada:"))

print("Tabuada do",num,"com For")
for i in range(1,11):
    print(num," x ",i, "=",(num*i))

print("\n Tabuada do", num,"com While:")
i = 1
while i > 0 and i < 11:
    print(num, "x", i, "=", (num*i))
    i+= 1