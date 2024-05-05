import random
import math

m = 4
eps = 0.005
t_a = 2.576
P = 0.995
N = int(t_a * t_a * P * (1 - P) / (eps * eps))
n = [4, 2, 6, 4]
lambda_ = [40e-6, 10e-6, 80e-6, 30e-6]
def main():
    T = 8760
    print(N)
    print(lambda_)
    for i in range(8):
        for j in range(8):
            for k in range(8):
                for l in range(8):
                    L = [i, j, k, l]
                    p_ = p(T, L)
                    if p_ > P:
                        print(L, "\tP =", p_, "\tN = ", sum(L))

def p(T, L):
    d = 0
    for nn in range(N):
        x = []
        for i in range(m):
            t = []
            for j in range(n[i]):
                t.append(-math.log(random.random()) / lambda_[i])
            for j in range(L[i]):
                l = t.index(min(t))
                t[l] -= math.log(random.random()) / lambda_[i]
            for j in range(n[i]):
                x.append(t[j])
        arr = [a for a in x]
        if not F(arr, T):
            d += 1
    return 1 - d / N

def F(t, T):
    return ((t[0] > T and t[1] > T or t[2] > T and t[3] > T) and t[4] > T and t[5] > T
            and (t[6] > T and t[7] > T or t[8] > T and t[9] > T or t[10] > T and t[11] > T) and (
                        t[12] > T or t[13] > T) and (t[14] > T or t[15] > T))

main()
