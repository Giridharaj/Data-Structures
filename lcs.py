def lcs(x,y):
    m,n=len(x),len(y)
    #! dp[i][j]=length of LCS of x[:i] and y[:j]
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(x[i-1]==y[j-1]):
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    i,j=m,n
    result=[]
    while(i>0 and j>0):
        if(x[i-1]==y[j-1]):
            result.append(x[i-1])
            i-=1
            j-=1
        elif(dp[i-1][j]>=dp[i][j-1]):
            i-=1
        else:
            j-=1
    result.reverse()
    return dp[m][n],''.join(result)

if __name__=='__main__':
    x='AGGTAB'
    y='GXTXAYB'
    length,subsequence=lcs(x,y)
    print("String 1: ",x)
    print("String 2: ",y)
    print("Length of LCS: ",length)
    print("Longest Common Subsequence: ",subsequence)