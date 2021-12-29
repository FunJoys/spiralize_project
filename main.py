
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



    arr = np.zeros(shape=(n, n))
    num1 = nums()
    t = 1
    for i in range(0, len(num1)):
        if t == 4:
            t -= 2
        for j in range(num1[i]):
            arr[0, j] = 1
        arr = np.rot90(arr, 1)
        t += 1
    print(arr)


print(spiralize(10))


