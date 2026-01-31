from collections import deque

def valid(m, c):
    return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c)

def solve():
    start, goal = (3,3,1), (0,0,0)
    moves = [(2,0),(0,2),(1,1),(1,0),(0,1)]
    q = deque([(start, [])])
    seen = set()

    while q:
        (m,c,b), path = q.popleft()
        if (m,c,b) in seen: 
            continue
        seen.add((m,c,b))
        path = path + [(m,c,b)]

        if (m,c,b) == goal:
            return path

        for dm,dc in moves:
            nm, nc = (m-dm, c-dc) if b else (m+dm, c+dc)
            if valid(nm,nc) and valid(3-nm,3-nc):
                q.append(((nm,nc,1-b), path))

for s in solve():
    print(s)
