for andar in range(20, 0, -1):
    if andar == 13:
        continue
    print(andar)

andar = 20
while andar > 0:
    if andar != 13:
        print(andar)
    andar -= 1

andar = 20
while True:
    if andar != 13:
        print(andar)
    andar -= 1
    if andar == 0:
        break