if __name__ == "__main__":
    
    # boj.kr/17136
    
    arr = [input().split() for _ in range(10)]
    dp = [[[0, i, j, False] for j in range(len(arr[0]))] for i in range(10)]

    for i in range(len(arr[0])):
        if arr[0][i] == "1":
            dp[0][i][0] = 1

    for i in range(1, 10):
        if arr[i][0] == "1":
            dp[i][0][0] = 1
        for j in range(1, len(arr[0])):
            if arr[i][j] == "1":
                dp[i][j][0] = min(dp[i][j-1][0], dp[i-1][j][0], dp[i-1][j-1][0]) + 1
                if dp[i][j][0] >= 5:
                    dp[i][j][0] = 5

    size = 5

    while size >=1:
        for i in range(10):
            for j in range(len(dp[0])):
                sum = 0            
                if dp[i][j][0] == size:                
                    for k in range(size-1, -1, -1):
                        for l in range(size-1, -1, -1):
                            if not dp[i-k][j-k][3]:
                                sum += 1                                             
                                        
                if sum == size ** 2:                              
                    for k in range(size-1, -1, -1):
                        for l in range(size-1, -1, -1):
                            dp[i-k][j-l][3] = True                            
                            if not(k==0 and l==0) :                      
                                dp[i-k][j-l][0] = 0
        size -= 1
        
    sum = 0
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            if dp[i][j][0] != 0:
                sum += 1
            
    print(sum)      
    
    """
    # boj.kr/1915
    n, m = map(int, input().split())

    arr = [input() for _ in range(n)]
    dp = [[0] * m for _ in range(n)]

    for i in range(m):
        if arr[0][i] == "1":
            dp[0][i] = 1
            
    for i in range(1, n):    
            if arr[i][0] == "1":
                dp[i][0] = 1
            for j in range(1, m):
                if arr[i][j] == "1":
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    
    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(ans, dp[i][j])

    print(ans ** 2)
    """    

    """    
    # boj.kr/1389
    from collections import deque

    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x : x-1, map(int, input().split()))
        adj[a].append(b)
        adj[b].append(a)
        
    kevin = []  
    ans = (-1, N ** 2)  

    def bfs(start, goal):
        chk = [False] * N
        chk[start] = True
        
        dq = deque()
        dq.append((start, 0))
        
        while dq:
            now, d = dq.popleft()
            if now == goal:
                return d
            nd = d + 1
            for nxt in adj[now]:
                if not chk[nxt]:
                    chk[nxt] = True
                    dq.append((nxt, nd))
                    
    def get_kevin(start):
        tot = 0
        for i in range(N):
            if i != start:
                tot += bfs(start, i)
        return tot

    for i in range(N):
        kevin.append(get_kevin(i))
        
    for i, v in enumerate(kevin):
        if ans[1] > v:
            ans = (i, v)
            
    print(ans[0] + 1)
    """
    
    """   
    #boj.kr/15686
    from itertools import combinations

    N, M = map(int, input().split())  # (5, 2)
    city = [[0] * N for _ in range(N)]

    for i in range(N):

        for j, cell in enumerate(map(int, input().split())):
            city[i][j] = cell
        
    chicken_dict = {}
    for i in range(N):
        for j in range(N):
            if city[i][j] == 2:
                chicken_dict['chicken_' + str(i) + str(j)] = (i, j)
                
    house_dict = {}
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                house_dict['house_' + str(i) + str(j)] = (i, j)
                
    def measure_dist(tuple1, tuple2):
        dist = abs(tuple1[0] - tuple2[0]) + abs(tuple1[1] - tuple2[1])
        return dist
                
    city_distances = []

    for num_ch in range(1, M+1):    
        for c in combinations(chicken_dict.items(), num_ch):
            dist = 0
            for name, coord in house_dict.items():
                cc_list = []
                
                for i in range(len(c)):                
                    cc_dist = measure_dist(c[i][1], coord)                
                    cc_list.append(cc_dist)
                min_cc_dist = min(cc_list)        
                
                dist += min_cc_dist
            city_distances.append(dist)        
            
        min_city_distance = min(city_distances)
        
    print(min_city_distance) 
    """            
                  
    """
    #boj.kr/4796
    for i in range(3):    
        L, P, V = map(int, input().split())
        if i < 2:
            full_use, incomplete_use = (V // P) * L, V % P
            total_use = full_use + incomplete_use
            print(f"Case {i+1}: {total_use}")
    """
    
    """
    # boj.kr/1018
    N, M = map(int, input().split())
    board = [[0] * M for _ in range(N)]

    for i in range(N):
        row = input()
        for j in range(M):
            board[i][j] = row[j]
        
    board = [[0 if board[i][j] == "W" else 1 for j in range(len(board[i]))] for i in range(len(board))]
        
    white_row = [0, 1, 0, 1, 0, 1, 0, 1]
    black_row = [1, 0, 1, 0, 1, 0, 1, 0]

    white_chess = [white_row, black_row] * 4
    black_chess = [black_row, white_row] * 4
        
    trial_rows = N - 8 + 1
    trial_cols = M - 8 + 1

    white_diffs = [[0] * trial_cols for _ in range(trial_rows)]    
    black_diffs = [[0] * trial_cols for _ in range(trial_rows)]
        
    for i in range(trial_rows):
        for j in range(trial_cols):
            for k in range(8):
                for l in range(8):
                    if white_chess[k][l] != board[i+k][j+l]:
                        white_diffs[i][j] += 1
                    if black_chess[k][l] != board[i+k][j+l]:
                        black_diffs[i][j] += 1
                        
    white_min = min([min(x) for x in white_diffs])
    black_min = min([min(x) for x in black_diffs])
    overall_min = min(white_min, black_min)

    print(overall_min)
    """
    
    """
    # boj.kr/2841 
    import sys
    import heapq as hq
    
    input = sys.stdin.readline

    pq = [[] for _ in range(500_000)]
    N, P = map(int, input().split())
    ans = 0

    for _ in range(N):
        String, Fret = map(int, input().split())    
        
        for _ in range(len(pq[String-1])) :
            if -Fret > min(pq[String-1]):
                hq.heappop(pq[String-1])
                ans += 1
        
        if -Fret not in pq[String-1]:    
            hq.heappush(pq[String-1], -Fret)
            ans += 1    
                
    print(ans)          
    """

