# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque

def BFS():
	que=deque()
	que.append(1)
	global cnt
	while que:
		cur=que.popleft()
		for j in arr[cur]:
			if visited[j] == 0 :
				visited[j]=1
				cnt+=1
				que.append(j)
	return cnt

N=int(input())
M=int(input())

arr = [[] for _ in range(N+1)]
visited = [0]*(N+1)
cnt=0
for M in range(M):
	a,b=map(int, sys.stdin.readline().split())
	arr[a].append(b)
	arr[b].append(a)
#print(arr)
visited[1]=1
res=BFS()
print(res)
