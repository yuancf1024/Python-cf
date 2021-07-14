# 程序分析：用字符串解决。
#%%
a = input("被加数字: ") # a代表字符串

n = int(input("加几次？: "))

res = 0

for i in range(n):
    res += int(a)
    a += a[0] # a[0]代表字符串，2+2='22'
    # print(a)
print("结果是: ", res)

#%%
import sys
list = []  
list_new = [] 
# sys.stdin.readline()
for line in sys.stdin:      
     list_new = line.split()
     list.append(list_new) 
     print(list)
# %%
