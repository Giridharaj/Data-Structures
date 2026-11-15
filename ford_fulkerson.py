def ford_fulkerson(capacity,source,sink):
    n=len(capacity)
    residual=[row[:] for row in capacity]
    max_flow=0

    def dfs(u,t,flow,visited):
        if u==t:
            return flow
        visited[u]=True
        for v in range(n):
            if not visited[v] and residual[u][v]>0:
                min_flow=min(flow,residual[u][v])
                pushed=dfs(v,t,min_flow,visited)
                if pushed>0:
                    residual[u][v]-=pushed
                    residual[v][u]+=pushed
                    return pushed
        return 0

    while True:
        visited=[False]*n
        pushed=dfs(source,sink,float('inf'),visited)
        if pushed==0:
            break
        max_flow+=pushed

    return max_flow

cap=[
    [0,10,0,0],
    [0,0,2,4],
    [0,0,0,9],
    [0,0,0,0]
]
print("Maximum flow: ",ford_fulkerson(cap,0,3))