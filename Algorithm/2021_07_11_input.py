a,b,c=[int(i) for i in input().split()]

hangshu = c

list=[]

for i in range(hangshu):
    # list.append([int(i) for i in input().split()])
    list.extend([int(i) for i in input().split()])
print(list)