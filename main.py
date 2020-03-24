from math import log
a = input()
b = []

for i in range(int(a)):
    b.append(int(input()))


def sumLessPowersOfTwo(N):
    # Sum of an AP is (n/2)*(a + l)
    sumToN = int((N*(1 + N))//2)
    # Sum of a GP is (a(r^n - 1)/(r-1), and a = 1, r - 1 = 1
    # r = 2, and to find n
    n = int(log(N, 2) + 1)
    sumOfTwos = (2**n)-1
    return sumToN - 2*sumOfTwos

for i in b:
    print(sumLessPowersOfTwo(i))
