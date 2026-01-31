N = 8
pos = [-1] * N

def safe(r, c):
    for i in range(r):
        if pos[i] == c or abs(pos[i] - c) == r - i:
            return False
    return True

def solve(r):
    if r == N:
        for i in range(N):
            print(" ".join("Q" if pos[i]==j else "." for j in range(N)))
        return True

    for c in range(N):
        if safe(r, c):
            pos[r] = c
            if solve(r + 1):
                return True
            pos[r] = -1

solve(0)
