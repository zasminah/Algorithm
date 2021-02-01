#https://www.acmicpc.net/problem/2178
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#import sys
from queue import Queue
from sys import stdin

def BFS(que):
	direct=[[1,0],[-1,0],[0,1],[0,-1]]
	global Y,X
	que.put((0,0,1)) #y,x,t
	while (not que.empty()):
		y,x,t=que.get()		
		if y==(Y-1) and x==(X-1):
			return t
		for i in range(4):
			dy=y+direct[i][0]
			dx=x+direct[i][1]
			if dy>=Y or dy<0 or dx>=X or dx<0:
				continue
			if visited[dy][dx] == 1 : 
				continue
			# if arr[dy][dx] == 0 :
			if arr[dy][dx] == '0':
				continue 
			visited[dy][dx]=1	
			que.put((dy,dx,t+1))
	return -1
	
que=Queue()
# Y,X=map(int, stdin.readline().split())
# arr = [[0 for _ in range(X)] for _ in range(Y)]
# visited = [[0 for _ in range(X)] for _ in range(Y)]
# for i in range(Y):
#     line=stdin.readline().strip()
#     for j,v in enumerate(line):
#         arr[i][j]=int(v)
Y, X = map(int, stdin.readline().split())
arr = [stdin.readline().rstrip() for _ in range(Y)] #possible with String Type
visited = [[0]*X for _ in range(Y)]

res = BFS(que)
print(res)
