c0 = int(input("Choose a number:"))
steps = 0

while c0 <= 0 :
    print("Number cannot  be below 0")
    c0 = int(input("Choose a number:"))
else:
    while c0 != 1:
        print(c0)
        steps += 1
        if c0 % 2 == 0 :
            c0 = c0 / 2
        elif c0 % 2 != 0 :
            c0 = 3 * c0 + 1


print(c0)
print("it took",steps, "Steps")
