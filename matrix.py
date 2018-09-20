weight = 'false'
directed = 'false'
begin = 'false'
build = 'false'
end = 'false'
vertices = []
adjMatrix = []


def build_matrix(line):
    global adjMatrix
    print('In the build matrix', line)
    a = [0] * len(vertices)
    for i in range(len(vertices)):
        a[i] = [0] * len(vertices)
    adjMatrix = a


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
        print('begin after',begin)
    elif begin == 'true' and build == 'false':
        vertices = line
        build = 'true'
        print('assigned vertices', vertices)
        build_matrix(line)
        print('the matrix is built', adjMatrix)
    elif begin == 'true' and build == 'true':
        print('add edge', line)
    elif line[0] == 'end':
        end = 'true'


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
