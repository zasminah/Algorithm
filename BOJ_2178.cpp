//https://www.acmicpc.net/problem/2178
#include <iostream>
using namespace std;

#define MAX ((int)100)
char map[MAX+10][MAX+10];
int visited[MAX+10][MAX+10];

int Y,X;

struct QUE{
	int y;
	int x;
	int t;
};

QUE que[MAX*MAX+10];
int wp,rp;

void push(int y, int x, int t){
	que[wp].y=y; que[wp].x=x;que[wp].t=t;
	wp++;
}
void pop(){rp++;}
QUE front(){return que[rp];}
int empty(){return wp==rp;}

int direct[4][2]={1,0,
								 -1,0,
								 0,1,
								 0,-1};

int BFS(int s, int e, int t){
	wp=rp=0;
	push(s,e,t);
	while(rp!=wp){
		QUE cur = front();pop();
		if(cur.y==(Y-1) && cur.x==(X-1)) return cur.t;
		for(int i=0;i<4;i++){
			int dy=cur.y+direct[i][0];
			int dx=cur.x+direct[i][1];
			if(dy<0||dx<0||dy>=Y||dx>=X)continue;
			if(visited[dy][dx]==1)continue;
			if(map[dy][dx]=='0')continue;
			visited[dy][dx]=1;
			push(dy,dx,cur.t+1);
		}
	}
	return -1;
}
int main() {
	cin>>Y>>X;
	for(int y=0;y<Y;y++){
		cin>>map[y];
	}
	int res = BFS(0,0,1);
	cout<<res;
	return 0;
}