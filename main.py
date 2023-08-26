if __name__ == "__main__":
    
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

