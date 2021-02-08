#https://www.acmicpc.net/problem/1726
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque

def BFS():
	que=deque()
	visited[sY-1][sX-1][sD]=0
	que.append([sY-1,sX-1,sD])
	while que :
		y,x,d=que.popleft()
		#print(y,x,d)
		if y==(eY-1) and x==(eX-1) and d==eD :
			return visited[eY-1][eX-1][d]
		
		#Same direction Go 1 2 3
		for i in range(1,4):
			dy=y+i*direct[d-1][0] # Same direction 1~3 
			dx=x+i*direct[d-1][1] # Same direction 1~3 
			if dy<0 or dx<0 or dy>=Y or dx>=X : continue # Out of range
			if  arr[dy][dx] == 1:	break # Cannot jump 

			if visited[dy][dx][d] == -1:
				visited[dy][dx][d] = visited[y][x][d]+1
				que.append([dy,dx,d])
		
		#Different direction at Same Postion
		for i in directRL[d-1]:
			if visited[y][x][i] == -1:
				visited[y][x][i] = visited[y][x][d]+1
				que.append([y,x,i])
		
	return -1
				
Y,X = map(int, sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(Y)]
visited = [[[-1]*5 for _ in range(X)] for _ in range(Y)]
direct = [[0,1],[0,-1],[1,0],[-1,0]]
directRL=[[4,3],[4,3],[1,2],[1,2]]
#direction E:1 W:2 S:3 N:4
sY,sX,sD=map(int, sys.stdin.readline().split())
eY,eX,eD=map(int, sys.stdin.readline().split())

res = BFS()
print(res)