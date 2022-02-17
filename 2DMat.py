import math
if __name__ == '__main__':
    r,c = map(int,input().split())
    a = []
    for i in range(r):
        row = list(map(int,input().split()[:c]))
        a.append(row)
    print(a)