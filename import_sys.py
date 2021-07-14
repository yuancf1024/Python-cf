nums = int(input())
points = []
for i in range(0, nums):   
    read_list = list(map(int, input().split()))   
 # read_list = [int(i) for i in input().split()]   
    points.append((read_list[0], read_list[1]))

print(points)
"""
3
1 2
23 4
4 5
[(1, 2), (23, 4), (4, 5)]
"""
