from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        print(x, y)

        # Stop only when final state is (2, 0)
        if x == target and y == 0:
            print("Target reached")
            return

        queue.extend([
            (jug1, y),      
            (x, jug2),      
            (0, y),         
            (x, 0),         
            (min(x+y, jug1), max(0, x+y-jug1)),  
            (max(0, x+y-jug2), min(x+y, jug2))   
        ])

water_jug(4, 3, 2)
