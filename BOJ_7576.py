#https://www.acmicpc.net/problem/7576
#https://otugi.tistory.com/60
#python의 queue 모듈은 멀티쓰레드를 처리하기 위한 동기화 과정을 거치기 때문에 collections.deque보다 느리다.
#from queue import Queue
from collections import deque
from sys import stdin
			
t=0
def BFS(que):
	direct = [[1,0],[-1,0],[0,1],[0,-1]]
	global Y,X			
	#while not que.empty():
	while que:
		#y,x,t = que.get()
		y,x,t = que.popleft()
		for i in range(4):
			dy=y+direct[i][0]
			dx=x+direct[i][1]
			if dy<0 or dy>=Y or dx<0 or dx>=X :
				continue
			if arr[dy][dx] != 0 :
				continue
			if visited[dy][dx] == 1 :
				continue
			visited[dy][dx]=1
			arr[dy][dx]=1
			#que.put((dy,dx,t+1))
			que.append([dy,dx,t+1])
	return t

#que=Queue() 
que=deque()
X,Y=map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(Y)]
visited = [[0]*X for _ in range(Y)]

for y in range(Y):
	for x in range(X):
		if arr[y][x] == 1 :
			visited[y][x]=1
			que.append([y,x,0])

res = BFS(que)

for y in range(Y):
	for x in range(X):
		if arr[y][x] == 0 :
			res = -1

print(res)
	

