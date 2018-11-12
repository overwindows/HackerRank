#!/bin/python3
import math
import os
import random
import re
import sys
import time

def DFS(root, val, graph, visits, node_cnt, uniedges, invert):
    visits[root] = 1
    for node in graph[root]:
        if visits[node] == 0:
            uniedges.append([root, node])
            n = len(uniedges) - 1
            v,c = DFS(node, val, graph, visits, node_cnt, uniedges, invert)
            if v not in invert:
                invert[v] = []
            invert[v].append(n)
            val[root] += v
            node_cnt[root] += c
    return val[root], node_cnt[root]

# Complete the balancedfatherNode function below.
def balancedfatherNode(c, edges):
    node_cnt = [1] * len(c)
    minimum_val = sys.maxsize
    _sum = sum(c)
    graph= {}
    treeVal = c
    
    if len(c) < 3:
        return -1
    
    for edge in edges:
        a, b = edge
        if a-1 in graph:
            graph[a-1].append(b-1)
        else:
            graph[a-1] = [b-1]
        
        if b-1 in graph:
            graph[b-1].append(a-1)
        else:
            graph[b-1] = [a-1]
    
    visits = [0] * len(c)
    uniedges = []
    invert = {}
    DFS(0, treeVal, graph, visits, node_cnt, uniedges, invert)
      
    for i in range(len(uniedges)-1):
        _, c = uniedges[i]            
        c_tree_val = treeVal[c]
        p_tree_val = _sum - c_tree_val

        # Special case. one cut.
        if c_tree_val == p_tree_val and c_tree_val < minimum_val:
            minimum_val = c_tree_val
            continue
        
        if (3 * min(c_tree_val, p_tree_val) - _sum) > minimum_val:
            continue
        
        if _sum > 2 * c_tree_val:
            #print("p > c", p_tree_val, c_tree_val)
            if p_tree_val // 2 < c_tree_val:
                expect = c_tree_val
            else:
                if p_tree_val % 2:
                    continue
                expect = p_tree_val // 2
            
            isMatch = False
            
            if expect in invert:
                for ix in invert[expect]:
                    if ix < len(uniedges) and ix >=i + node_cnt[c]:
                        isMatch = True
                        break
            
            if p_tree_val - expect in invert:
                for ix in invert[p_tree_val - expect]:
                    if ix < len(uniedges) and ix >=i + node_cnt[c]:
                        isMatch = True
                        break
            
            if isMatch:
                _min = 3*expect - _sum
                minimum_val = min(_min,minimum_val)    
            '''
            for j in range(i + node_cnt[c], len(uniedges)):
                _, _c = uniedges[j]
                sub_tree0 = treeVal[_c]
                sub_tree1 = p_tree_val - sub_tree0
                
                if sub_tree1 != expect and sub_tree0 != expect:
                    continue
                
                print(expect)
                _min = 3 * expect - _sum
                minimum_val = min(_min,minimum_val)
            '''
        else: 
            #print("c > p")
            if c_tree_val // 2 < p_tree_val:
                expect = p_tree_val
            else:
                if c_tree_val % 2:
                    continue
                expect = c_tree_val // 2
            
            '''
            if expect in invert:
                for ix in invert[expect]:
                    if ix < i + node_cnt[c] and ix >=i + 1:
                        print(expect)
            
            if c_tree_val - expect in invert:
                for ix in invert[c_tree_val - expect]:
                    if ix < i + node_cnt[c] and ix >=i + 1:
                        print(expect)
            '''
            
            for j in range(i + 1, i + node_cnt[c]):
                # Reset stat
                _c_tree_val = c_tree_val

                _, _c = uniedges[j]
                cc_tree_val = treeVal[_c]
                _c_tree_val -= cc_tree_val
                
                if _c_tree_val != expect and cc_tree_val != expect:
                    continue
                
                #print(expect)
                _min = 3*expect - _sum
                minimum_val = min(_min,minimum_val)

    if minimum_val == sys.maxsize:
        return -1
    else:
        return minimum_val    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        result = balancedfatherNode(c, edges)

        fptr.write(str(result) + '\n')

    fptr.close()
