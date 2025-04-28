x = 50
y = 130

if x > y:
    print("x é maior que y")
    if x - y > 10:
        print("A diferença entre x e y é maior que 10")
    else:
        print("A diferença entre x e y é menor ou igual a 10")
elif x < y:
    print("x é menor que y")
    if y - x > 5:
        print("y é significativamente maior que x")
    else:
        print("A diferença entre y e x não é tão grande")
else:
    print("x é igual a y")
