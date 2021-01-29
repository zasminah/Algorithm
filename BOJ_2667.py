#https://www.acmicpc.net/problem/2667
import sys
N=int(input())
matrix=[[0 for col in range(N)] for low in range(N)]
visited=[[0 for col in range(N)] for low in range(N)]

for i in range(N):
    line=sys.stdin.readline().strip()
    for j,v in enumerate(line):
        matrix[i][j]=int(v)

#print(matrix) # for debugging

direct = [[-1,0],[1,0],[0,-1],[0,1]]

def floodfill(y,x):
    if y>=N or y<0 or x>=N or x<0:
        return
    if visited[y][x] == 1:
        return
    if matrix[y][x] == 0:
        return

    visited[y][x]=1
    global nums
    #global cnt # for debugging
    nums+=1
    #matrix[y][x]=cnt # for debugging

    for i in range(4):
        dy=y+direct[i][0]
        dx=x+direct[i][1]
        floodfill(dy,dx)

cnt=0 # Number of Apartment complex
numlist=[] # Storage nums for each complex
nums=0 # Number of Apartment

for y in range(N):
    for x in range(N):
        if matrix[y][x] == 1 and visited[y][x] == 0:
            cnt+=1
            floodfill(y,x)
            #print(y,x,nums) # for debugging
            numlist.append(nums)
            nums=0
#print(matrix) # for debugging
print(len(numlist))
for n in sorted(numlist):
    print(n)