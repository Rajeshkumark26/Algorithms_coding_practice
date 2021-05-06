grid = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]
k = 2
S = 14
N=4

def getSum(r1,r2,c1,c2,dp):
    return dp[r2][c2]-dp[r2][c1]-dp[r1][c2]+dp[r1][c1]


def sumFound(grid,S,k,N):
    
    dp = [[0 for j in range(N + 1)] for i in range(N +1)]

    for i in range(N):
        for j in range(N):
            dp[i+1][j+1]= dp[i+1][j]+dp[i][j+1]-dp[i][j]+grid[i][j]

    for i in range(N):
        for j in range(N):
            sum_=getSum(i,i+k,j,j+k,dp)
            if sum_==S:
                return True            
    return False

sumFound(grid,S,k,N)