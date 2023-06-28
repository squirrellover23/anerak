import math


num_nodes, num_queries = (int(i) for i in input().split())
edges = [[1, None, []]]
for i in range(num_nodes - 1):
    info = [int(i) for i in input().split()]
    listOfConnections = edges[min(info) - 1][2] + [max(info)]
    edges.append([max(info), min(info), listOfConnections])
sets = []
for i in range(num_queries):
    b = input()
    sets.append([int(i) for i in input().split()])



def distance(node1, node2):
    n1 = edges[node1-1]
    n2 = edges[node2-1]
    dis = len(n1[2]) + len(n2[2])
    for i in range(min(len(n1[2]), len(n2[2]))):
        if n1[2][i] == n2[2][i]:
            dis -= 2
        else:
            return dis
    return dis


for s in sets:
    sumTotal = 0
    if len(s) < 2:
        print(0)
    else:
        for numOn in range(1, len(s)):
            for numPair in range(0, numOn):
                sumTotal += s[numOn] * s[numPair] * distance(s[numPair], s[numOn])
        sumTotal %= (10**9 + 7)
        print(sumTotal)
