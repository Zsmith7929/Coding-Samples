# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math

def main(max_prime):

    num = 11
    primes = [2,3,5,7,11]
    while len(primes) < max_prime:
        num += 1
        prime = True
        for x in xrange(2,int(math.sqrt(num))+1):
            if num%x != 0:
                continue
            else:
                prime = False
                break

        if prime:
            primes.append(num)
            print "%d is prime" % num

    print primes

if __name__ == "__main__":
    main(10001)
        
