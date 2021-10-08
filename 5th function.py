import random
random_number = random.randint(1,201)

m = 1
n = random.randint(max(random_number, 50), 201)
print(f"the range for this round is {m}-{n}")

while True:
    a = int(input("make a guess: "))
    if a < random_number:
        m = a
        print(f"the range is now {m} - {n}")
    elif a > random_number:
        n = a
        print(f"the range is now {m} - {n}")
    else:
        print("BINGO!")
        break
