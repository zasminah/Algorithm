#https://www.acmicpc.net/problem/2206
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque

def BFS():
	visited[0][0][0] = 1 #visited[flag][y][x] = cnt
	que=deque() 
	que.append([0,0,0])#y,x,flag
	while que :
		y,x,flag=que.popleft()
		if y==(Y-1) and x==(X-1):
			return visited[y][x][flag]
		for i in range(4):
			dy=y+direct[i][0]
			dx=x+direct[i][1]
			if dy<0 or dx<0 or dy>=Y or dx>=X :
				continue
			if arr[dy][dx] == 1 and flag == 0 :
				visited[dy][dx][flag+1] = visited[y][x][flag]+1
				que.append([dy,dx,flag+1])
			elif arr[dy][dx] == 0 and visited[dy][dx][flag]==0 :
				visited[dy][dx][flag] = visited[y][x][flag]+1
				que.append([dy,dx,flag])
	return -1

Y,X = map(int, sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().strip())) for _ in range(Y)]
visited = [[[0]*2 for _ in range(X)] for _ in range(Y)] #visited[y][x][flag] = cnt
direct =[[-1,0],[1,0],[0,-1],[0,1]]

#print(arr)
res=BFS()
print(res)