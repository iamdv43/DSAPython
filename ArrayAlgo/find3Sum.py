def find3Sum(n, A, X):
    A.sort()
    for i in range(n - 1):
        l = i + 1
        r = n - 1
        while l < r:
            if A[i] + A[l] + A[r] == X:
                return True
            elif A[i] + A[l] + A[r] > X:
                r -= 1
            else:
                l += 1
    return False


arr = [1, 4, 45, 6, 10, 8]
X= 13
print(find3Sum(len(arr), arr, X))