weight = 'false'
directed = 'false'
begin = 'false'
build = 'false'
end = 'false'
vertices = []
verticesLink = []
verticesWeight = []
files = []


# Returns the index based on vertices list
def get_index(vertex):
    index = 0
    for i in range(len(vertices)):
        if vertices[i] == vertex:
            index = i
    return index


# Build an empty list of lists of vertices length size
def build_link_list(line):
    a = []
    print('In the build matrix', line)
    for i in range(len(vertices)):
        a.append([])
    return a


# Returns true or false if edge is in the link list
def has_edge(line):
    vertex1 = line[0]
    vertex2 = line[1]
    ans = 'false'
    vertex_index1 = int(get_index(vertex1))
    for i in range(len(verticesLink[vertex_index1])):
        if vertex2 == verticesLink[vertex_index1][i]:
            ans = 'true'
            return ans
    return ans


# Partitions the line removing addEdge
def part_line(line):
    line2 = []
    for i in range(1, len(line)):
        line2.append(line[i])
    return line2


# Adds edge is there is no edge already
def add_edge(line):
    global verticesLink
    global verticesWeight
    vertex1 = line[0]
    vertex2 = line[1]
    vertex_index1 = int(get_index(vertex1))
    vertex_index2 = int(get_index(vertex2))
    weight_val = float(0.0)
    check = has_edge(line)
    print('IS there that edge?',check)
    if check == 'false':
        if weight == 'true':
            weight_val = float(line[2])
            vertex_index1 = int(get_index(vertex1))
            vertex_index2 = int(get_index(vertex2))
        if directed == 'true':
            verticesWeight[vertex_index1].append(weight_val)
            verticesLink[vertex_index1].append(vertex2)
        elif directed == 'false':
            verticesLink[vertex_index1].append(vertex2)
            verticesWeight[vertex_index1].append(weight_val)
            verticesLink[vertex_index2].append(vertex1)
            verticesWeight[vertex_index2].append(weight_val)


# Deletes edge based on direction
def delete_edge(line):
    global verticesLink
    global verticesWeight
    vertex1 = line[0]
    vertex2 = line[1]
    vertex_index1 = int(get_index(vertex1))
    vertex_index2 = int(get_index(vertex2))
    if directed == 'true':
        for i in range(len(verticesLink[vertex_index1])):
            if vertex2 == verticesLink[vertex_index1][i]:
                del verticesLink[vertex_index1][i]
                del verticesWeight[vertex_index1][i]
                return 'true'
    else:
        for i in range(len(verticesLink[vertex_index1])):
            if vertex2 == verticesLink[vertex_index1][i]:
                del verticesLink[vertex_index1][i]
                del verticesWeight[vertex_index1][i]
        for i in range(len(verticesLink[vertex_index2])):
            if vertex1 == verticesLink[vertex_index2][i]:
                del verticesLink[vertex_index2][i]
                del verticesWeight[vertex_index2][i]
                return 'true'
    return 'false'


# Return number of vertexes in graph
def count_vertices():
    return len(vertices)


# Returns number of edges in graph
def count_edges():
    count = 0
    for i in range(len(verticesWeight)):
        for j in range(len(verticesWeight[i])):
            if verticesWeight[i][j] > -1:
                count += 1
    return count


# Returns the max number of edges in graph
def max_edges():
    return len(vertices) * (len(vertices)-1)


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


# Returns true or false if graph is fully connected
def is_fully_connected():
    max = max_edges()
    edges = count_edges()
    if (edges / max) == 1:
        return 'true'
    return 'false'


# Return true or false if vertex is in Vertices list
def has_vertex(line):
    for i in range(len(vertices)):
        if line == vertices[i]:
            return 'true'
    return 'false'


# Returns true or false when vertex is added
def add_vertex(line):
    global vertices
    global verticesLink
    global verticesWeight
    yes_no = has_vertex(line[1])
    if yes_no == 'true':
        return 'false'
    else:
        vertices.append(line[1])
        verticesLink.append([])
        verticesWeight.append([])
        return 'true'


# Delete vertex from vertices and link lists
def delete_vertex(line):
    global vertices
    yes_no = has_vertex(line[1])
    if yes_no == 'false':
        return 'false'
    else:
        vertex = get_index(line[1])
        for i in range(len(verticesLink)):
            for j in range(len(verticesLink[i])):
                if line[1] == verticesLink[i][j]:
                    del verticesLink[i][j]
                    del verticesWeight[i][j]
        del verticesLink[vertex]
        del verticesWeight[vertex]
        vertices.remove(line[1])
        return 'true'


# print graph in linked list format
def print_graph():
    string = ''
    for i in range(len(files)):
        print(files[i])
    for i in range(len(verticesLink)):
        string += vertices[i]
        for j in range(len(verticesLink[i])):
            string += '->'
            string += verticesLink[i][j]
            string += '->'
            string += str(verticesWeight[i][j])
        print(string)
        string = ''


# determines if graph is connected
def is_connected():
    been = [0] * len(vertices)
    for i in range(len(vertices)):
        for j in range(len(verticesLink[i])):
            vertex = verticesLink[i][j]
            index_val = get_index(vertex)
            been[index_val] = 1
            print (vertex, index_val, been)
    if 0 in been:
        return "false, the graph isn't connected"
    return "true, graph is connected"


def function_calls(line):
    if line[0] == 'hasEdge':
        print("checking to have an edge at", line[1], line[2])
        line2 = part_line(line)
        yes_no = has_edge(line2)
        print(line, yes_no)
    elif line[0] == 'addEdge':
        line2 = part_line(line)
        yes_no = has_edge(line2)
        if yes_no == 'true':
            edge = 'false'
        else:
            add_edge(line2)
            edge = 'true'
        print(line, edge, verticesLink, verticesWeight)
    elif line[0] == 'deleteEdge':
        line2 = part_line(line)
        yes_no = has_edge(line2)
        if yes_no == 'false':
            edge = 'false'
        else:
            edge = delete_edge(line2)
        print(line, edge, verticesLink, verticesWeight)
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
        print(line, ans, vertices, verticesLink, verticesWeight)
    elif line[0] == 'deleteVertex':
        ans = delete_vertex(line)
        print(line, ans, vertices, verticesLink, verticesWeight)
    elif line[0] == 'readGraph':
        graph()
    elif line[0] == 'isConnected':
        ans = is_connected()
        print(line, ans)


# sets up program to run based on file line read
def execute(line):
    global verticesLink
    global verticesWeight
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
        verticesLink = build_link_list(line)
        verticesWeight = build_link_list(line)
        print('the linked list is built', verticesLink, verticesWeight)
    elif line[0] == 'end':
        end = 'true'
        begin = 'false'
        build = 'false'
    elif begin == 'true' and build == 'true':
        print('add edge', line)
        add_edge(line)
        print('Matrix with added edge', verticesLink, verticesWeight)
    elif end == 'true':
        function_calls(line)


def graph():
    global files
    fileName = input('Enter the file name: ')
    file = open(fileName, 'r')
    for line in file:
        line = line.strip('\n')
        if line[0] == '*':
            print('>>>>', line)
            print("Do Nothing")
        else:
            files.append(line)
            statements = line.split(' ')
            print('>>>>', statements)
            execute(statements)
    print('------------------------------------------------')
    file.close()


if __name__== '__main__':
    graph()
    print_graph()
