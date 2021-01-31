#https://www.acmicpc.net/problem/11724
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
sys.setrecursionlimit(10000) #need for runtime error


def dfs(i):
	visited[i]=1
	for j in arr[i]:
		if visited[j] == 0 :
			#visited[j]=1
			dfs(j)

#N,M=map(int, input().split())
N,M=map(int, sys.stdin.readline().split())
arr=[[] for _ in range(N+1)]
visited=[0]*(N+1)
cnt=0

for i in range(M):
	#s,e=map(int, input().split())
	s,e=map(int, sys.stdin.readline().split()) #resolve time exceed error
	arr[s].append(e)
	arr[e].append(s)
	
for i in range(1,N+1):
	if visited[i] == 0 :
		cnt+=1
		#visited[i]=1
		dfs(i)

print(cnt)




