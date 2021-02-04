#https://www.acmicpc.net/problem/2583
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
sys.setrecursionlimit(10000)

def DFS(y,x):
	global cnt
	cnt+=1
	for i in range(4):
		dy = y+ direct[i][0]
		dx = x+ direct[i][1]
		if dy<0 or dx<0 or dy>=Y or dx>=X :
			continue
		if arr[dy][dx] == 0:
			arr[dy][dx]=-1 #visited 
			DFS(dy,dx)
		
Y,X,K = map(int, sys.stdin.readline().split())
arr=[[0]*X for _ in range(Y)]
direct = [[1,0],[-1,0],[0,-1],[0,1]]
result = []
cnt=0

for k in range(K):
	sx,sy,ex,ey=map(int, sys.stdin.readline().split())
	for y in range(sy,ey):
		for x in range(sx,ex):
			arr[y][x]=1

for y in range(Y):
	for x in range(X):
		if arr[y][x] == 0 :
			cnt=0
			arr[y][x]=-1 #visited 
			DFS(y,x)
			result.append(cnt)
#print(arr)		
print(len(result))
#print(arr)
for i in sorted(result):
	print(i,end=' ')