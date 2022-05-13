def trappingWater(arr, n):
    sums = 0
    for i in range(1, n - 1):
        if i > 1:
            leftWall = max(arr[0:i])
        else:
            leftWall = arr[0]
        if i < n - 2:
            rightWall = max(arr[i + 1:])
        else:
            rightWall = arr[n - 1]
        maxH = min(leftWall, rightWall)
        if maxH > arr[i]:
            sums += (maxH - arr[i])
    return sums


arr = [1, 1, 5, 2, 7, 6, 1, 4, 2, 3]
print(trappingWater(arr, len(arr)))