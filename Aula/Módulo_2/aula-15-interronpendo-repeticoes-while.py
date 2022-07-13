# comando break
n = s = 0
while True:
    n = int(input("Digite um número: "))
    s += n
    if n < 1:
        break
print(f"A soma vale {s}")