def is_prime(n):
    avval = True
    for i in range(2, n // 2+1):
        if n % i == 0 :
            avval = False
    return avval

prime_count=0
for i in range(1,10001):
    if is_prime(i):
        prime_count = prime_count + 1
        print(i)
print ("we had", prime_count, "prime numbers")