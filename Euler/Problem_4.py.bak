# A palindromic number reads the same both ways.
# The largest palindrome made from the product
# of two 2-digit numbers is 9009 = 91 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome():
    
    products = set()

    for x in xrange(900,999):
        for y in xrange(900,999):
            temp = x*y
            n = [_x for _x in str(temp)]
            if temp not in products:
                if len(n)%2 == 0:
                    half = len(n)/2
                    first = n[:half]
                    last = n[half:]
                    last.reverse()
                    if first == last:
                        products.add(temp)

    return products



if __name__ == "__main__":
    n = palindrome()
    print n
                
        
