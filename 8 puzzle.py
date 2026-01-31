import heapq

GOAL_STATE = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

DIRECTIONS = [(-1,0), (1,0), (0,-1), (0,1)]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

def a_star(start_state):
    pq = []
    heapq.heappush(pq, (manhattan_distance(start_state), 0, start_state, []))
    visited = set()

    while pq:
        _, cost, state, path = heapq.heappop(pq)

        if state == GOAL_STATE:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_cost = cost + 1
                priority = new_cost + manhattan_distance(neighbor)
                heapq.heappush(pq, (priority, new_cost, neighbor, path + [state]))
    return None

start_state = (
    (1, 2, 3),
    (4, 0, 6),
    (7, 5, 8)
)

solution = a_star(start_state)

if solution:
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found")
