//https://www.acmicpc.net/problem/1987
#include <iostream>
using namespace std;

#define MAX ((int)20)
char arr[MAX+10][MAX+10];
int visited[100];
int Y,X;

int direct[4][2]={-1,0,
								 1,0,
								 0,-1,
								 0,1};

int res=1;

void DFS(int y, int x, int t){
	res=max(res,t);	
	//cout<<y<<" "<<x<<" "<<arr[y][x]<<" "<<t<<endl;
	for(int i=0;i<4;i++){
		int dy = y+direct[i][0];
		int dx = x+direct[i][1];
		if(dy<0||dx<0||dy>=Y||dx>=X)continue;
		if(visited[arr[dy][dx]]==1)continue;
		visited[arr[dy][dx]]=1;
		DFS(dy,dx,t+1);
		visited[arr[dy][dx]]=0;
	}
}

int main(){
	cin>>Y>>X;
	for(int y=0;y<Y;y++){
		cin>>arr[y];
	}
	
	visited[arr[0][0]]=1;
	DFS(0,0,1);
	
	cout<<res;
	
	return 0;
}