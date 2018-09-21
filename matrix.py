weight = 'false'
directed = 'false'
begin = 'false'
build = 'false'
end = 'false'
vertices = []
adjMatrix = []


# Returns the max number of edges in graph
def max_edges():
    return len(vertices) * (len(vertices)-1)


# Return number of edges in matrix
def count_edges():
    count = 0
    for i in range(len(adjMatrix)):
        for j in range(len(adjMatrix)):
            if adjMatrix[i][j] > 0:
                count += 1
    return count


# Returns true or false if graph is 0.15 or less
def is_sparse():
    max = max_edges()
    edges = count_edges()
    if (edges / max) <= 0.15:
        return 'true'
    return 'false'


# Returns true or false if graph is 0.85 or more
def is_dense():
    max = max_edges()
    edges = count_edges()
    if (edges / max) >= 0.85:
        return 'true'
    return 'false'


def is_fully_connected():
    max = max_edges()
    edges = count_edges()
    if (edges / max) == 1:
        return 'true'
    return 'false'


# Return number of vertexes in vertices list
def count_vertices():
    return len(vertices)


# Returns the index if vertex is found in vertices
def get_index(vertex):
    index = 0
    for i in range(len(vertices)):
        if vertices[i] == vertex:
            index = i
    return index


# add edge to adjMatrix, adjusts for weighted and directed
def add_edge(line):
    global adjMatrix
    vertex1 = line[0]
    vertex2 = line[1]
    weight_val = 1
    if weight == 'true':
        weight_val = float(line[2])
    vertex_index1 = int(get_index(vertex1))
    vertex_index2 = int(get_index(vertex2))
    if directed == 'true':
        adjMatrix[vertex_index1][vertex_index2] = weight_val
    elif directed == 'false':
        adjMatrix[vertex_index1][vertex_index2] = weight_val
        adjMatrix[vertex_index2][vertex_index1] = weight_val


# Build an empty list of lists of vertices length size
def build_matrix(line):
    global adjMatrix
    print('In the build matrix', line)
    a = [0] * len(vertices)
    for i in range(len(vertices)):
        a[i] = [0] * len(vertices)
    adjMatrix = a


# Build an empty list of lists of vertices length size
def make_matrix():
    a = [0] * len(vertices)
    for i in range(len(vertices)):
        a[i] = [0] * len(vertices)
    return a


def update_matrix():
    global adjMatrix
    a = make_matrix()
    for i in range(len(adjMatrix)):
        for j in range(len(adjMatrix)):
            if adjMatrix[i][j] > 0:
                a[i][j] = adjMatrix[i][j]
    adjMatrix = a


# Checks for an edge in Matrix, returns true or false
def has_edge(line):
    vertex1 = get_index(line[1])
    vertex2 = get_index(line[2])
    vertex1 = int(vertex1)
    vertex2 = int(vertex2)
    if adjMatrix[vertex1][vertex2] > 0:
        return 'true'
    return 'false'


# partitions the line for weighted
def part_line(line):
    line2 = []
    for i in range(1, len(line)):
        line2.append(line[i])
    return line2


# Deletes edge for directed and undirected
def delete_edge(line):
    global adjMatrix
    vertex1 = line[0]
    vertex2 = line[1]
    vertex_index1 = int(get_index(vertex1))
    vertex_index2 = int(get_index(vertex2))
    if directed == 'true':
        adjMatrix[vertex_index1][vertex_index2] = 0
        return 'true'
    else:
        adjMatrix[vertex_index1][vertex_index2] = 0
        adjMatrix[vertex_index2][vertex_index1] = 0
        return 'true'


# Returns true or false if vertex in vertices
def has_vertex(vertex):
    if vertex in vertices:
        return 'true'
    return 'false'


# Returns true or false if vertex is added to vertices
def add_vertex(line):
    global vertices
    yes_no = has_vertex(line[1])
    if yes_no == 'true':
        return 'false'
    else:
        vertices.append(line[1])
        update_matrix()
        return 'true'


def shift(index):
    global adjMatrix
    for i in range(len(adjMatrix)):
        for j in range(index, len(adjMatrix)-1):
            adjMatrix[i][j] = adjMatrix[i][j+1]
    for i in range(index, len(adjMatrix)-1):
        for j in range(len(adjMatrix)):
            adjMatrix[i][j] = adjMatrix[i+1][j]
    a = make_matrix()
    for i in range(len(a)):
        for j in range(len(a)):
            a[i][j] = adjMatrix[i][j]
    adjMatrix = a


# Returns true or false if vertex is removed from vertices
def delete_vertex(line):
    global vertices
    yes_no = has_vertex(line[1])
    if yes_no == 'false':
        return 'false'
    else:
        index = get_index(line[1])
        vertices.remove(line[1])
        shift(index)
        return 'true'


# After 'end', nested if else to call different functions
def function_calls(line):
    if line[0] == 'hasEdge':
        print("checking to have an edge at", line[1], line[2])
        yes_no = has_edge(line)
        print(line, yes_no)
    elif line[0] == 'addEdge':
        yes_no = has_edge(line)
        if yes_no == 'true':
            edge = 'false'
        else:
            line2 = part_line(line)
            add_edge(line2)
            edge = 'true'
        print(line, edge)
    elif line[0] == 'deleteEdge':
        yes_no = has_edge(line)
        if yes_no == 'false':
            edge = 'false'
        else:
            line2 = part_line(line)
            edge = delete_edge(line2)
        print(line, edge)
    elif line[0] == 'countVertices':
        num = count_vertices()
        print('Number of vertices in graph', num)
    elif line[0] == 'countEdges':
        num = count_edges()
        print('Number of edges in matrix', num)
    elif line[0] == 'isSparse':
        ans = is_sparse()
        print(line, ans)
    elif line[0] == 'isDense':
        ans = is_dense()
        print(line, ans)
    elif line[0] == 'isFullyConnected':
        ans = is_fully_connected()
        print(line, ans)
    elif line[0] == 'addVertex':
        ans = add_vertex(line)
        print(line, ans, vertices, adjMatrix)
    elif line[0] == 'deleteVertex':
        ans = delete_vertex(line)
        print(line, ans, vertices, adjMatrix)


# sets up program to run based on file line read
def execute(line):
    global weight
    global directed
    global begin
    global vertices
    global build
    global end
    if line[0] == 'weighted':
        weight = 'true'
        print('weighted after', weight)
    elif line[0] == 'directed':
        directed = 'true'
        print('directed after', directed)
    elif line[0] == 'begin':
        begin = 'true'
        print('begin after', begin)
    elif begin == 'true' and build == 'false':
        vertices = line
        build = 'true'
        print('assigned vertices', vertices)
        build_matrix(line)
        print('the matrix is built', adjMatrix)
    elif line[0] == 'end':
        end = 'true'
        begin = 'false'
        build = 'false'
    elif begin == 'true' and build == 'true':
        print('add edge', line)
        add_edge(line)
        print('Matrix with added edge', adjMatrix)
    elif end == 'true':
        function_calls(line)


if __name__ == '__main__':

    fileName = input('Enter the file name: ')
    file = open(fileName, 'r')
    for line in file:
        line = line.strip('\n')
        if line[0] == '*':
            print('>>>>', line)
            print("Do Nothing")
        else:
            statements = line.split(' ')
            print('>>>>', statements)
            execute(statements)
    print('------------------------------------------------')
    file.close()
