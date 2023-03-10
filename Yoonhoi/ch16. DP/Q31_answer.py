for tc in range(int(input())):
    n,m  = map(int,input().split())
    array = list(map(int,input().split()))
    
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index +=m
        
    # 그래프에 넣는 것. 
    
    
    # 첫번째 줄은 건들지 말고, 두번째 컬럼부터 진행한다. 
    for j in range(1,m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우, 예외 처리 
            if i == 0 :
                left_up = 0
            else:
                left_up = dp[i-1][i-1]
            
            # 맨 마지막에서 오는 경우  
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            
            # 현재 줄에서 오는 경우 예외 없음     
            left = dp[i][j-1] 
            # 그중 제일 큰 값과 더해주면 된다. 
            dp[i][j] = dp[i][j] + max(left_up,left_down,left) 
            
    result = 0
    for i in range(n):
        result = max(result,dp[i][m-1])
        
    print(result)