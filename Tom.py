### Fonction qui trie des tuples en fonction de leur deuxième élément ###

def sort_tuples_by_second_element(input_list):
    if not input_list:
        return []
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list of tuples")
    for item in input_list:
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Input list must contain 2-element tuples")
        if not isinstance(item[1], (int, float)):
            raise ValueError("Second element of tuple must be a number")
    if len(set([x[1] for x in input_list])) != len(input_list):
        raise ValueError("Input list contains duplicates")

    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i][1] < right[j][1]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

    def merge_sort(input_list):
        if len(input_list) <= 1:
            return input_list
        mid = len(input_list) // 2
        left = input_list[:mid]
        right = input_list[mid:]
        return merge(merge_sort(left), merge_sort(right))

    return merge_sort(input_list)

def test_sort_tuples_by_second_element():
    # Test Case 1
    assert sort_tuples_by_second_element([(1,2), (3,1), (4,5)]) == [(3,1), (1,2), (4,5)]

    # Test Case 2
    assert sort_tuples_by_second_element([(1,5), (2,5), (3,5)]) == [(1,5), (2,5), (3,5)]

    # Test Case 3
    assert sort_tuples_by_second_element([(3,5), (1,2), (2,1)]) == [(2,1), (1,2), (3,5)]

    # Test Case 4
    assert sort_tuples_by_second_element([]) == []

    # Test Case 5
    try:
        sort_tuples_by_second_element("not a list")
    except TypeError:
        pass
    else:
        raise AssertionError("TypeError not raised for non-list input")

    # Test Case 6
    try:
        sort_tuples_by_second_element([(1,2), (3,1), (4,5,6)])
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError not raised for invalid tuple length")



### Fonction qui trouve le chemin le plus court entre deux points dans un graphe pondéré représenté par un dictionnaire ###

def find_shortest_path(graph, start, end):
    if not isinstance(graph, dict):
        raise TypeError("Graph must be a dictionary")

    if start not in graph or end not in graph:
        raise ValueError("Start and end nodes must be in the graph")

    unvisited_nodes = {node: float('inf') for node in graph}
    unvisited_nodes[start] = 0
    previous_nodes = {node: None for node in graph}

    def get_smallest_unvisited_node():
        smallest_distance = float('inf')
        smallest_node = None

        for node, distance in unvisited_nodes.items():
            if distance < smallest_distance:
                smallest_distance = distance
                smallest_node = node

        return smallest_node

    current_node = get_smallest_unvisited_node()

    while current_node is not None:
        current_distance = unvisited_nodes[current_node]

        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight

            if new_distance < unvisited_nodes[neighbor]:
                unvisited_nodes[neighbor] = new_distance
                previous_nodes[neighbor] = current_node

        del unvisited_nodes[current_node]
        current_node = get_smallest_unvisited_node()

    path = []
    current_node = end

    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]

    return path[::-1]

# Test avec des entrées valides
input_list = [(2, 4), (5, 1), (3, 9), (7, 6)]
expected_output = [(5, 1), (2, 4), (7, 6), (3, 9)]
assert sort_tuples_by_second_element(input_list) == expected_output

# Test avec des listes d'entrée de différentes tailles
input_list = [(2, 4)]
expected_output = [(2, 4)]
assert sort_tuples_by_second_element(input_list) == expected_output

input_list = []
expected_output = []
assert sort_tuples_by_second_element(input_list) == expected_output

input_list = [(2, 4), (5, 1), (3, 9), (7, 6), (1, 5), (4, 8)]
expected_output = [(5, 1), (1, 5), (2, 4), (7, 6), (4, 8), (3, 9)]
assert sort_tuples_by_second_element(input_list) == expected_output

# Test avec des listes d'entrée déjà triées
input_list = [(2, 4), (5, 1), (7, 6), (3, 9)]
expected_output = [(5, 1), (2, 4), (7, 6), (3, 9)]
assert sort_tuples_by_second_element(input_list) == expected_output

# Test avec des listes d'entrée inversées
input_list = [(3, 9), (7, 6), (5, 1), (2, 4)]
expected_output = [(5, 1), (2, 4), (7, 6), (3, 9)]
assert sort_tuples_by_second_element(input_list) == expected_output

# Test avec des listes d'entrée contenant des nombres réels et entiers
input_list = [(2, 4.1), (5, 1.9), (3, 9), (7, 6.3)]
expected_output = [(5, 1.9), (2, 4.1), (7, 6.3), (3, 9)]
assert sort_tuples_by_second_element(input_list) == expected_output

