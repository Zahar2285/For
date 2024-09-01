numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True
for number in numbers:
    if is_prime(number):
        primes.append(number)
    else:
        not_primes.append(number)
print("Prime:", primes)
print("Not Prime:", not_primes)