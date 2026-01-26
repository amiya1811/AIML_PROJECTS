graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

h = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0
}

S = 'A'
G = 'D'

OPEN = [S]

g = {S: 0}

parent = {S: None}

while OPEN:
    current = min(OPEN, key=lambda x: g[x] + h[x])

    if current == G:
        print("Goal reached")
        break

    OPEN.remove(current)

    for neighbor, cost in graph[current]:
        new_cost = g[current] + cost

        if neighbor not in g or new_cost < g[neighbor]:
            g[neighbor] = new_cost
            parent[neighbor] = current
            OPEN.append(neighbor)
else:
    print("No route found")

path = []
node = G
while node is not None:
    path.append(node)
    node = parent[node]

path.reverse()
print("Path:", path)
