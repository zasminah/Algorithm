//https://www.acmicpc.net/problem/2667
//FloodFill

#include <iostream>
#include <cstdlib>
using namespace std;
int N;
#define MAX ((int)625)
char map[25+10][25+10];
int visited[25+10][25+10];

int direct[4][2]={
	1,0,
	-1,0,
	0,1,
	0,-1
};
int build[MAX+10];
int cnt;
void FloodFill(int y, int x){
	if(y<0||y>=N||x<0||x>=N)return;
	if(visited[y][x]==1)return;
	if(map[y][x]!='1')return;
	visited[y][x]=1;
	map[y][x]='0';
	cnt++;
	for(int i=0;i<4;i++){
		int dy=y+direct[i][0];
		int dx=x+direct[i][1];
		FloodFill(dy,dx);
	}
}

int compare(const void* a, const void* b){
	return *(int *)a-*(int *)b;
}

int main(){

	int count=0;
	int sol=0;
	cin>>N;
	for(int i=0;i<N;i++){
		cin>>map[i];
	}
	for(int y=0;y<N;y++){
		for(int x=0; x<N;x++){
			if(map[y][x]=='1'){
				count++;
				cnt=0;
				FloodFill(y,x);
				build[sol++]=cnt;
			}
		}
	}
	cout<<count<<endl;
	qsort(build,sol,sizeof(build[0]),compare);
	for(int i=0;i<sol;i++){
		cout<<build[i]<<endl;
	}
	return 0;
}