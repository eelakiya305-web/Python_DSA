def checkPrime(n):
    cnt = 0  

    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1  
    return cnt == 2


n = 1483  
isPrime = checkPrime(n)  
if isPrime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
