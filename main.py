
import numpy as np




def spiralize(n):


    def nums():
        n1 = [n, n, n]
        if n % 2 != 0:
            for i in reversed(range(3, n-1, 2)):
                n1 += [i]
                n1 += [i]
        else:
            for i in reversed(range(4, n-1, 2)):
                n1 += [i]
                n1 += [i]
                if i == 4:
                    n1 += [2]
        return n1

    def rows(f, num1):
        t = []
        z = 0
        b = True
        while b:
            for i in range(f):
                if len(t) != len(num1):
                    t.append(z)
                else:
                    b = False
                    break
            z += 2
        return t


    arr = np.zeros(shape=(n, n))
    num1 = nums()
    num2 = rows(4, num1)
    num3 = rows(5, num1)
    print(num1)
    print(num2)
    print(num3)

    for m in range(len(num1)):
        for k in range(num3[m], num3[m]+num1[m]):
            print(num2[m], k)
            arr[num2[m], k] = 1
        arr = np.rot90(arr)
    arr = np.rot90(arr, n)
    print(arr)


print(spiralize(6))