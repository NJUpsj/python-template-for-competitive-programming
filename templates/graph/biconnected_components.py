import math
import sys


def input(): return sys.stdin.readline().strip()  # fast IO


from functools import cmp_to_key


def LII():
    return list(map(int, input().split()))


def TII():
    return tuple(map(int, input().split()))


from collections import deque

from collections import defaultdict
from bisect import bisect_left
import random
from collections import deque
import heapq

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc



def solve():
    n,m=LII()
    graph=[[] for ii  in range(n)]
    for i in range(m):
        a,b=LII()
        a,b=a-1,b-1
        graph[a].append(b)
        graph[b].append(a)
    nodev=[0]*n
    stack=[0]
    visit=[0]*n
    visit[0]=1
    fals=[-1]*n
    sontreenum=[1]*n
    s=[]
    visitedge=set()
    while stack:
        node=stack.pop()
        s.append(node)
        for son in graph[node]:
            if son != fals[node] and not visit[son]:
                stack.append(son)
                fals[son]=node
                visit[son]=1
            elif son!= fals[node] and visit[son]:
                if (son,node) in visitedge or (node,son) in visitedge:
                    continue
                nodev[son]+=1
                nodev[node]-=1
                visitedge.add((son,node))
    s.reverse()
    sumtreenodev = [0] * n
    result=n*(n-1)//2
    for son in s:
        sumtreenodev[son] += nodev[son]
        if fals[son]>=0:
            sumtreenodev[fals[son]] += sumtreenodev[son]
            sontreenum[fals[son]]+=sontreenum[son]
        if sumtreenodev[son]==0:
            x=sontreenum[son]
            result=min(result,x*(x-1)//2+(n-x)*(n-x-1)//2)
    print(result)

for i in range(int(input())):
    # for i in range(1):
    solve()