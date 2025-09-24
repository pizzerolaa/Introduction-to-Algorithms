# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

def is_happy(n: int) -> bool:
        aux = set()
        while n not in aux:
            if n == 1:
                return True
            aux.add(n)
            tot = 0
            while n > 0:
                tot += (n%10)**2
                n //= 10
            n = tot
        return False

n = 19
print(is_happy(n))