import math
if __name__ == '__main__':
   # math function significance
   #  a = math.gcd(2,3)
   #  print(a)
   #  b = math.gcd(10,15)
   # print(b)

    print("Euclid Algorithm :")
    x = int(input())
    y = int(input())

    while x != 0:
        x, y = y % x, x
    print("GCD is ",y)  
