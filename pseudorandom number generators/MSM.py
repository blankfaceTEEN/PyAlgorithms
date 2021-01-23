# Middle-square method
def generator(seed):
    number = list(str(seed))
    half = int(len(number) / 2)
    first_half = number[0:half]
    second_half = number[half:len(number)]
    random = int(first_half[len(first_half) - 1]) * 10 + int(second_half[0])
    return random * random


x = 8649

for i in range(100):
    x = generator(x)
    print(x)

