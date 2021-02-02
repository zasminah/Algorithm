//https://www.acmicpc.net/problem/7576
#include <iostream>
using namespace std;

#define MAX ((int)1000)
int arr[MAX+10][MAX+10];
int visited[MAX+10][MAX+10];

struct QUE{
	int y,x,t;
};

QUE que[MAX*MAX+10];
int wp,rp;
int Y,X;
int direct[4][2]={-1,0,
								 1,0,
								 0,-1,
								 0,1};

void push(int y, int x, int t){
	que[wp].y=y; que[wp].x=x; que[wp].t=t;
	wp++;
}
void pop(){rp++;}
QUE front(){return que[rp];}
int empty(){return wp==rp;}

int BFS(){
	rp=wp=0;
	
	for(int y=0;y<Y;y++){
		for(int x=0;x<X;x++){
			if(arr[y][x]==1){
				visited[y][x]=1;
				push(y,x,0);
			}
		}
	}
	
	QUE cur;
	while(!empty()){
		cur = front(); pop();
		for(int i=0;i<4;i++){
			int dy=cur.y+direct[i][0];
			int dx=cur.x+direct[i][1];
			if(dy<0||dy>=Y||dx<0||dx>=X) continue;
			if(arr[dy][dx]!=0) continue;
			if(visited[dy][dx]==1)continue;
			visited[dy][dx]=1;
			arr[dy][dx]=1;
			push(dy,dx,cur.t+1);
		}
	}
	return cur.t;
}

int main(){
	cin>>X>>Y;
	for(int y=0;y<Y;y++){
		for(int x=0;x<X;x++){
			cin>>arr[y][x];
		}
	}
	int res=BFS();
	
	for(int y=0;y<Y;y++){
		for(int x=0;x<X;x++){
			if(arr[y][x]==0){
				cout<<-1;
				return 0;
			}
		}
	}	
	cout<<res;
	return 0;
}