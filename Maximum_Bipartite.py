def max_bipartite(graph,num_left,num_right):
    '''
        graph: adjacency list where graph[u]=list of right vertices
            that left vertex u is connnected to.
        Returns: (matching size,match_right)
            match_right[v]=left vertex matched to right vertex v (or -1)
    '''
    match_right=[-1]*num_right

    def try_augment(u,visited):
        for v in graph[u]:
            if not visited[v]:
                visited[v]=True
                if match_right[v]==-1 or try_augment(match_right[v],visited):
                    match_right[v]=u
                    return True
        return False

    result=0
    for u in range(num_left):
        visited=[False]*num_right
        if try_augment(u,visited):
            result+=1
    return result,match_right

if __name__=='__main__':
    graph=[[0,1],[0,2],[1,2],[2,3]]
    size,match_right=max_bipartite(graph,3,4)
    print("Maximum matching size: ",size)
    print("Matching pairs (left -> right): ")
    for v,u in enumerate(match_right):
        if u!=-1:
            print(f"{u}->{v}")