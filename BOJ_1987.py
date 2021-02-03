#ord : Return ASCII Value (wikidocs.net/32#ord)
#Rambda : Functiion (wikidocs.net/64)
#Submit as PYPY3

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#from sys import stdin
import sys
sys.setrecursionlimit(10000)

direct=[[1,0],[-1,0],[0,1],[0,-1]]

def DFS(y,x,t):
	global res
	res=max(res,t)
	for i in range(4):
		dy=y+direct[i][0]
		dx=x+direct[i][1]
		if dy<0 or dx<0 or dy>=Y or dx>=X :
			continue
		if visited[arr[dy][dx]] == 1:
			continue
		visited[arr[dy][dx]]=1
		DFS(dy,dx,t+1)
		visited[arr[dy][dx]]=0
		# if arr[dy][dx] in visited :
		# 	continue
		# visited.append(arr[dy][dx])
		# DFS(dy,dx,t+1)
		# visited.remove(arr[dy][dx])
		
res=1
Y,X=map(int, sys.stdin.readline().split())
#arr=[list(sys.stdin.readline().strip()) for _ in range(Y)]
arr=[list(map(lambda x : ord(x)-65,sys.stdin.readline().strip())) for _ in range(Y)] # ASCII
visited=[0]*26

# visited.append(arr[0][0])
visited[arr[0][0]]=1
DFS(0,0,1)
print(res)
