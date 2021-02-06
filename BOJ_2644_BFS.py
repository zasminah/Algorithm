# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#https://www.acmicpc.net/problem/2644
#Refer to https://www.acmicpc.net/problem/11724
import sys
from collections import deque

def BFS():
	que=deque()
	que.append([A,0])
	while que:
		cur,cnt=que.popleft()
		if cur == B :
			return cnt
		
		for i in family[cur]:
			if visited[i] == 0:
				visited[i]=1
				que.append([i,cnt+1])
	return -1

N = int(input())
A,B = map(int, sys.stdin.readline().split())
M = int(input())
family=[[] for _ in range(N+1)]
visited=[0]*(N+1)
for i in range(M):
	p,c=map(int,sys.stdin.readline().split())
	family[p].append(c)
	family[c].append(p)

#print(family)
visited[A]=1	
sol = BFS()
print(sol)