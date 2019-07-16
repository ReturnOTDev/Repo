import time


def calc(binary):
    binList = list(map(lambda x: int(x), binary))[::-1]
    decimal = 0

    for i in range(len(binList)):
        if binList[i] == 1:
            if i == 0:
                decimal += 1
            else:
                decimal += i ** 2

    return decimal
inp = input("Enter binary number here: ")
print(calc(inp))
time.sleep(10)