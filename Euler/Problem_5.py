# 2520 is the smallest number that can be divided by 
# each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly 
# divisible by all of the numbers from 1 to 20?

def main(r):
    
    div = range(1,r+1)
    
    for x in xrange(9999999,999999999):
        num = 0
        for n in div:
            if x%n == 0:
                num += 1
            
        if num >= 20:
            return x
            
            
if __name__ == "__main__":
    z = main(20)
    print z