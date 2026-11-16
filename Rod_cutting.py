def Rod_cutting(i,j,price,dp):
    if i==0 or j==0:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    take=0
    if i<=j:
        take=price[i]+Rod_cutting(i,j-i,price,dp)
    no_take=Rod_cutting(i-1,j,price,dp)
    dp[i][j]=max(take,no_take)
    return dp[i][j]

def Recur_Rod_Cutting(price):
    n=len(price)-1
    dp=[[-1]*(n+1) for _ in range(n+1)]
    return Rod_cutting(n,n,price,dp)

if __name__=='__main__':
    price=[0]+list(map(int,input('Enter the Price: ').split()))
    print(f"Max Obtainable value: {Recur_Rod_Cutting(price)}")