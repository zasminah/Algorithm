#https://www.acmicpc.net/problem/2234
import sys
from collections import deque
sys.setrecursionlimit(10**6)

def BFS(y,x,g):
	que=deque()
	que.append([y,x,g])
	global cnt
	while que :
		y,x,g=que.popleft()
		for i in range(4):
			if i == 0 and arr[y][x] & 4 : continue #EAST
			elif i == 1 and arr[y][x] & 1 : continue #WEST
			elif i == 2 and arr[y][x] & 8 : continue #SOUTH
			elif i == 3 and arr[y][x] & 2 : continue #NORTH
			
			dy=y+direct[i][0]
			dx=x+direct[i][1] 
			if dy<0 or dx<0 or dy>=Y or dx>=X: continue
			if visited[dy][dx] == 0 :
				visited[dy][dx]=g
				cnt+=1
				que.append([dy,dx,g])

def calcSumGroup(y,x) :
	if visitedG[y][x] == 1 :
		return
	visitedG[y][x]=1
	
	global val
	for i in range(4):
		dy=y+direct[i][0]
		dx=x+direct[i][1]
		if dy<0 or dx<0 or dy>=Y or dx>=X :
			continue
		if visited[dy][dx] == visited[y][x] :
			continue 
			#print(visited[dy][dx],visited[y][x])
		val=max(val, grouptLst[visited[dy][dx]-1]+grouptLst[visited[y][x]-1])
		calcSumGroup(dy,dx)	
				
X,Y = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(Y)]
direct = [[0,1],[0,-1],[1,0],[-1,0]]
visited = [[0]*X for _ in range(Y)]
visitedG = [[0]*X for _ in range(Y)]
grouptLst=[] 
group=0 #the # of Group
cnt=0 # the # of cell of Each Group
val=0 #MaxGroup with summation 

for y in range(Y):
	for x in range(X):
		if visited[y][x] == 0 :
			group+=1
			cnt=1
			visited[y][x]=group
			BFS(y,x,group)
			grouptLst.append(cnt)

for y in range(Y):
	for x in range(X):
		if visitedG[y][x] == 0 :
			calcSumGroup(y,x) # To get MaxGroup with summation 
		
print(len(grouptLst))
#grouptLst=sorted(grouptLst, key=lambda x:x[1], reverse=True) #Reverse sort
grouptLst.sort(reverse=True)
#print(grouptLst)
#print(visited)
print(grouptLst[0])
print(val)

