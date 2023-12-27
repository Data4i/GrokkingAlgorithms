graph = {
    'start': {
        'a': 6,
        'b': 2
    },
    'a': {
        'fin': 1
    },
    'b': {
        'a': 3,
        'fin': 5
    },
    'fin': {}
}

costs = {
    'a': 6,
    'b': 2,
    'fin': float('inf')
}

parents = {
    'a': 'start',
    'b': 'start',
    'fin': None
}

processed = []


def find_lowest_cost_node(d_costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for d_node in d_costs:
        d_cost = d_costs[d_node]
        if d_cost < lowest_cost and d_node not in processed:
            lowest_cost = d_cost
            lowest_cost_node = d_node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


print(processed, parents, costs)