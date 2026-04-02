import heapq

print("\nName: Your Name")
print("Register Number: Your Reg No")
print("UCS\n")

graph = {
    'A': [('B',1), ('C',4)],
    'B': [('D',2), ('E',5)],
    'C': [('F',1)],
    'D': [('G',1)],
    'E': [('G',1)],
    'F': [('G',3)],
    'G': []
}

pq = [(0,'A')]
visited = set()

# ADD THIS
parent = {'A': None}

while pq:
    cost,node = heapq.heappop(pq)

    if node == 'G':
        # RECONSTRUCT PATH
        path = []
        cur = node
        while cur:
            path.append(cur)
            cur = parent[cur]
        path.reverse()

        print("Path:", " -> ".join(path))
        print("Cost:", cost)
        break

    if node not in visited:
        visited.add(node)
        for n,w in graph[node]:
            # STORE PARENT
            if n not in parent:
                parent[n] = node
            heapq.heappush(pq,(cost+w,n))