import math

# a = list(map(int, input().split()))

a = [1, 43, 437, 978, 17268, 112, -1]
# print(a)
# print(min(a), max(a), sum(a), sum(a) / len(a))

for item in a:
    print(item)

    divisors = []
    for i in range(1, item + 1):
        if item % i == 0:
            divisors.append(i)
    print(divisors)

    primes = []
    for i in range(2, int(item ** 0.5) + 1):
        while item % i == 0:
            primes.append(i)
            item = item // i
            # item //= i
    if item > 1:
        primes.append(item)
    print(primes)

# for i in range(10):
#     print(i)

# for i in a:
#     print(i ** 2)

# s = 'abcdef'

# for c in s:
#     print(c)

a = math.sin(math.pi)
print(f'Hello, {a:.5f}!')

# s = input('What is your name? ')
# print(f'Hello, ' + s + '! Nice to meet you')

# a = list(map(int, a))

# for i in range(len(a)):
#     a[i] = int(a[i])
# print(a)