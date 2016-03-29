# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def find_triplet():
    
    



def main():

    z = 1
    while True:
        test = find_triplet(num=z)

        if sum(test) == 1000:
            return test
        

        z = test[1]
        print z



if __name__ == "__main__":

    triplet = main()

    print triplet
