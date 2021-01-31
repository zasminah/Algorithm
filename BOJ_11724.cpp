//https://www.acmicpc.net/problem/11724
#include <iostream>
using namespace std;

int arr[1000+10][1000+10];
int visited[1000+10];
int N,M;
int cnt;

void dfs(int i){
	for(int j=1;j<=N;j++){
		if(arr[i][j]==1 && visited[j]!=1){
			visited[j]=1;
			dfs(j);
		}
	}
}

int main() {
	cin>>N>>M;
	for(int i=0;i<M;i++){
		int s,e;
		cin>>s>>e;
		arr[s][e]=1;
		arr[e][s]=1;
	}
	
	for(int i=1;i<=N;i++){
		if(visited[i]==0){
			cnt++;
			visited[i]=1;
			dfs(i);
		}
	}
	
	cout<<cnt;
	return 0;
}