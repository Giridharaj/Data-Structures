import math

def optimal_bst(keys,p):
    n=len(keys)
    p=[0]+p
    c=[[0]*(n+2) for _ in range(n+2)]
    w=[[0]*(n+2) for _ in range(n+2)]
    root=[[0]*(n+2) for _ in range(n+2)]

    for L in range(1,n+1):
        for i in range(1,n-L+2):
            j=i+L-1
            w[i][j]=w[i][j-1]+p[i]
            best=math.inf
            for r in range(i,j+1):
                t=c[i][r-1]+c[r+1][j]
                if t<best:
                    best,root[i][j]=t,r
            c[i][j]=best+w[i][j]
    return c,root

def print_tree(keys,root,i,j,indent=0):
    if i>=j:
        return
    r=root[i][j]
    print_tree(keys,root,i,r-1,indent+4)
    print(" "*indent+keys[r-1])
    print_tree(keys,root,r+1,j,indent+4)

keys=['A','B','C','D','E','F','G','H','I','J']
freq=[4,5,7,5,6,3,5,8,4,2]
c,root=optimal_bst(keys,freq)
print("Optimal Binary Search Tree: ")
print("Optimal Cost: ",c[1][len(keys)])
print_tree(keys,root,1,len(keys),0)
