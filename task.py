#arthimatic operator 
a = 7#
b = 2
print(a + b)     # 9     addition
print(a - b)     # 5     subtraction
print(a * b)     # 14    multiplication
print(a / b)     # 3.5   division (always gives a float)
print(a // b)    # 3     floor division (drops the decimal part)
print(a % b)     # 1     modulus (remainder)
print(a ** b)    # 49    exponent (7 x 7)
#comparison operator 
x = 5
y = 3
print(x == y)    # False  equal to
print(x != y)    # True   not equal to
print(x > y)     # True   greater than
print(x < y)     # False  less than
print(x >= 5)    # True   greater than or equal to
print(y <= 2)    # False  less than or equal to
# assignment operator 
n = 10
print(n)         # 10   =
n += 5
print(n)         # 15   n = n + 5
n -= 3
print(n)         # 12   n = n - 3
n *= 2
print(n)         # 24   n = n * 2
n /= 4
print(n)         # 6.0  n = n / 4
n //= 4
print(n)         # 1.0  n = n // 4
n = 17
n %= 5
print(n)         # 2    n = n % 5
n **= 3
print(n)         # 8    n = n ** 3
#logical operator 
age = 20
has_id = True
print(age >= 18 and has_id)   # True   both must be true
print(age < 18 or has_id)     # True   at least one is true
print(not has_id)             # False  flips the value
 
# and / or return one of the values (truthy / falsy)
print(0 and 5)          # 0      first falsy value
print(3 and 5)          # 5      last value
print(0 or 5)           # 5      first truthy value
#bitwise operator
p = 5    # binary 101
q = 3    # binary 011
print(p & q)     # 1    AND   (001)
print(p | q)     # 7    OR    (111)
print(p ^ q)     # 6    XOR   (110)
print(~p)        # -6   NOT
print(p << 1)    # 10   left shift (doubles)
print(p >> 1)    # 2    right shift (halves)
#membership operator
print("a" in "apple")          # True
print("x" in "apple")          # False
print(3 in [1, 2, 3])          # True
print("x" not in "apple")      # True
print(10 not in [1, 2, 3])     # True
#identity operator
list1 = [1, 2]
list2 = [1, 2]
list3 = list1
print(list1 == list2)       # True   same values
print(list1 is list2)       # False  different objects in memory
print(list1 is list3)       # True   same object
print(list1 is not list2)   # True
 
value = None
print(value is None)        # True   (the usual way to check None)