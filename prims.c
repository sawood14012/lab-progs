/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int i,j,n;
    int cost[10][10];
    int a,b,u,v,min=0,mincost=0,visited[10]={0},ne=1;
    printf("enter the no of nodes\n");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
      for(j=1;j<=n;j++)
      {
          printf("enter the cost between %d and %d\n",i,j);
          scanf("%d",&cost[i][j]);
      }
      visited[1]=1;
      while(ne<n){
          min=999;
          for(i=1;i<=n;i++)
      for(j=1;j<=n;j++)
      if(cost[i][j]<min)
      if(visited[j]!=0)
      {
          min = cost[i][j];
          a=u=i;
          b=v=j;
      }
      if(visited[u]==0|visited[v]==0)
      {
          printf("node %d and node %d cost %d\n",a,b,min);
          ne=ne+1;
          mincost=mincost+min;
          visited[b]=1;
      }
          cost[a][b]=cost[b][a]=999;
      }
    printf("%d",mincost);
    
}
