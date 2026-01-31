def is_safe(region, color, assignment, neighbors):
    for n in neighbors[region]:
        if assignment.get(n) == color:
            return False
    return True

def solve_map(assignment):
    if len(assignment) == len(regions):
        return assignment

    region = [r for r in regions if r not in assignment][0]

    for color in colors:
        if is_safe(region, color, assignment, neighbors):
            assignment[region] = color
            result = solve_map(assignment)
            if result:
                return result
            del assignment[region]

    return None

# Regions and their neighbors
regions = ['A', 'B', 'C', 'D']
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

solution = solve_map({})

print("Map Coloring Solution:")
for r in solution:
    print(r, ":", solution[r])
