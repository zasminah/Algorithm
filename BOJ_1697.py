#https://www.acmicpc.net/problem/1697

from sys import stdin
from collections import deque

def BFS():
	que = deque()
	que.append([N,0])
	while que:
		n,t=que.popleft()
		if n == K :
			return t
		# for i in range(3):
		# 	if i==0 : dn=n+1
		# 	elif i==1 : dn=n-1
		# 	else : dn=n*2
		for i in (n+1,n-1,n*2):
			dn=i
			if dn<0 or dn>100000 or visited[dn]==1: 
				continue
			visited[dn]=1
			que.append([dn,t+1])
	return -1

#0<=N,K<=100000
N, K = map(int, stdin.readline().split())
visited=[0]*100001

res=BFS()
print(res)
