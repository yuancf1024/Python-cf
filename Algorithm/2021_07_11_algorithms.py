"""一些有趣的算法题汇总

"""

#%% 001-输入输出

'''
输入样例: 下面是两个测试样例

3 1
2 3 1
5 4
1 2 1
3 4 0
2 5 1
3 2 1

样例输出

0
3
'''

def run(res):
	"""这个函数写得很妙，细细体会"""
	visited = set()
	visited.add(1)
	res.sort()
	# 将与1有关系的，即与小赛是老乡的，则记录在集合里，以免重复记录
	for i in res:
		if i[0] in visited:
			visited.add(i[1])
	# 集合的长度减去小赛本人则为他的老乡人数
	return (len(visited) - 1)

def main():
	# while True的作用是连续输入多个测试样例，若题目没要求输入多个测试样例，
	# 则不需要使用whhile True
	#while True:
	res = []
	N, M = map(int, input().split())
	for i in range(M):
		a, b, c = map(int, input().split())
		# a,b若为老乡，则记录下来
		if c == 1:
			res.append([a, b] if a <b else [b, a] )
	result = run(res)
	print(res)
	print(result)
	return

main()