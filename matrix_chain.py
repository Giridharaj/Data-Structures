import sys
def matrix_chain_order(p):
    n=len(p)-1
    m=[[0]*(n+1) for _ in range(n+1)]
    s=[[0]*(n+1) for _ in range(n+1)]

    for L in range(2,n+1):
        for i in range(1,n-L+2):
            j=i+L-1
            m[i][j]=sys.maxsize
            for k in range(i,j):
                cost=m[i][k]+m[k+1][j]+(p[i-1]*p[k]*p[j])
                if cost<m[i][j]:
                    m[i][j]=cost
                    s[i][j]=k
    return m,s

def get_optimal_parens(s,i,j):
    if i==j:
        return f"A{i}"
    else:
        left=get_optimal_parens(s,i,s[i][j])
        right=get_optimal_parens(s,s[i][j]+1,j)
        return f"({left} * {right})"

if __name__=='__main__':
    p=list(map(int,input("Enter the dimensions of matrices (space-separated): ").split()))
    n=len(p)-1
    m,s=matrix_chain_order(p)
    min_ops=m[1][n]
    paren=get_optimal_parens(s,1,n)

    print(f"Minimum number of multiplications: {min_ops}")
    print(f"Optimal parenthesization: {paren}")