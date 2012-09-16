#!/usr/bin/env python

import sys
import re

def bfs(s, G):
    """Do a breadth-first search of graph G starting at node s and return the
    list of nodes reachable from s (from which you can infer their distances)
    along with the BFS tree created during execution of the search"""
    discovered = [False for i in range(len(G))]
    discovered[s] = True
    T = []
    L = [[s]]
    i = 0
    while len(L[i]) > 0:
        L.append([])
        for u in L[i]:
            for v in G[u]:
                if discovered[v] == False:
                    discovered[v] = True
                    T.append((u, v))
                    L[i+1].append(v)
        i += 1
    return (L, T)

def bfs2(s, G):
    "Single list implementation using a Queue, but no Layer list returned"
    discovered = [False for i in range(len(G))]
    discovered[s] = True
    T = []
    L = [s]
    i = 0
    while len(L) > 0:
        u = L.pop(0)
        for v in G[u]:
            if discovered[v] == False:
                discovered[v] = True
                T.append((u, v))
                L.append(v)
        i += 1
    return (L, T)

def dfs(s, G):
    """Do a depth-first search of graph G starting at node s and return the
    DFS tree created during execution of the search"""
    explored = [False for i in range(len(G))]
    parent = [None for i in range(len(G))]
    T = []
    S = [s]
    while len(S) > 0:
        u = S.pop()
        if explored[u] == False:
            explored[u] = True
            if u != s:
                T.append((parent[u], u))
            for v in G[u]:
                S.append(v)
                parent[v] = u
    return T

def usage():
    print "Usage: %s <input.graph>" % (sys.argv[0])

def check_args():
    if len(sys.argv) != 2:
        sys.exit(usage())

def read_input():
    "Read input and return as adjacency list"
    f = open(sys.argv[1], 'r')
    n = f.readline()
    while n.strip().startswith('#'):
        n = f.readline()
    source = f.read()
    # G[i] holds the adjacency list for node i
    G = [[] for i in range(int(n))]
    W = {}
    edges = re.findall('(\(.*?\))+', source)
    for e in edges:                    
        node = e.strip('()').split(',')
        if len(node) == 3:
            [u, v, weight] = node
        else:
            node.append(-1)
            [u, v, weight] = node
        # For a given edge {u, v}, u should be on v's adjacency list,
        # and v should be on u's
        G[int(u)].append(int(v))
        G[int(v)].append(int(u))
        W[(u, v)] = int(weight)
        W[(v, u)] = int(weight)
    return (G, W)

def run():
    check_args()
    (G, W) = read_input()
    for i in range(len(G)):
        (L, T) = bfs(i, G)
        print "Graph: %s" % (G)
        print "BFS(%d) Layers: %s" % (i, L)
        print "BFS(%d) Tree: %s" % (i, T)
        T = dfs(i, G)
        print "DFS(%d) Tree: %s" % (i, T)

if __name__ == '__main__':
    run()
