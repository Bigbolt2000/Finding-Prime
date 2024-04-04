# Find prime numbers
number = [1,2]
prime_num = []
for e in range(1, 25):
    if e not in number:
        prime_num.append(e)
    else:
        for i in range(1, 10):
            b = e * i
            number.append(b)

print(prime_num)
