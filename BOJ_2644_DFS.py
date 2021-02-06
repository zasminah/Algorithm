# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#https://www.acmicpc.net/problem/2644
#Refer to https://www.acmicpc.net/problem/11724
import sys
sys.setrecursionlimit(100000)

def DFS(i,cnt):
	#print(i,cnt)
	global sol
	# if cnt>=N : 
	# 	sol=-1
	# 	return
	if i==B :
		sol=cnt
		return

	for j in family[i] :
		if visited[j] == 0 :
			visited[j]=1
			DFS(j,cnt+1)
					
N = int(input())
A,B = map(int, sys.stdin.readline().split())
M = int(input())
family=[[] for _ in range(N+1)]
visited=[0]*(N+1)
for i in range(M):
	p,c=map(int,sys.stdin.readline().split())
	family[p].append(c)
	family[c].append(p)
sol=-1
#print(family)
visited[A]=1	
DFS(A,0)
print(sol)