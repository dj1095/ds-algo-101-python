
def cycleInGraph(edges):
    # Write your code here.
    no_of_vertices = len(edges)
    visited = [0 for _ in range(no_of_vertices)]
    in_stack = [0 for _ in range(no_of_vertices)]
    result = False
    for idx in range(no_of_vertices):
        result = result or depth_first_search(idx, edges, visited, in_stack)
        print(result)
    return result


def depth_first_search(idx, edges, visited, in_stack):
    visited[idx] = 1
    in_stack[idx] = 1
    print('Entered with edge' ,idx)
    print('visited' ,visited)
    print('instack' ,in_stack)
    print('Exploring out edges' ,edges[idx])
    if len(edges[idx]) == 0:
        print('Releasing from stack' ,idx)
        in_stack[idx] = 0
        return False
    for vertex in edges[idx]:
        print('Exploring out edge' ,vertex)
        if visited[vertex] == 1 and in_stack[vertex] == 1:
            print('Found Cycle')
            return True
        elif visited[vertex] == 0:
            return depth_first_search(vertex, edges, visited, in_stack)
    print('Releasing from stack' ,vertex)
    in_stack[idx] = 0
    return False


graph = [[],[0,3],[0],[1,2]]

cycleInGraph(graph)