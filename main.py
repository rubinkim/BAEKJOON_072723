if __name__ == "__main__":
    
    """
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

    # boj.kr/2841 
    import heapq as hq

    pq = [[] for _ in range(500_000)]

    N, P = map(int, input().split())

    ans = 0

    for _ in range(N):
        String, Fret = map(int, input().split())    
        print(f"String : {String},   Fret : {Fret}") 
        
        for _ in range(len(pq[String-1])) :
            if -Fret > min(pq[String-1]):
                hq.heappop(pq[String-1])
                ans += 1
        
        if -Fret not in pq[String-1]:    
            hq.heappush(pq[String-1], -Fret)
            ans += 1    
                
    print(ans)      
 