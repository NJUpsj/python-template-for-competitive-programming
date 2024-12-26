"""luogu 2863"""

import math
import sys


def input(): return sys.stdin.readline().strip()  # fast IO


from  typing import  *

def LII():
    return list(map(int, input().split()))


def TII():
    return tuple(map(int, input().split()))

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
    graph=[[] for i in range(n)]
    indgree=[0 for i in range(n)]
    for i in range(m):
        a,b=LII()
        a,b=a-1,b-1
        graph[a].append(b)
        indgree[b]+=1
    time=0
    dfn=[10**6]*n
    low=[10**6]*n
    intarjanstack=[0]*n
    tarjanstack=[]
    scc=[0]*n
    scccnt=1
    @bootstrap
    def tarjan(node):
        nonlocal time
        nonlocal scccnt
        time+=1
        dfn[node]=time
        low[node]=time
        tarjanstack.append(node)
        intarjanstack[node]=1

        for son in graph[node]:
            if dfn[son]==10**6:
                r1=yield  tarjan(son)
                low[node]=min(low[node],low[son])
            elif intarjanstack[son]:
                low[node]=min(low[node],dfn[son])
        if low[node]==dfn[node]:
            while tarjanstack:
                popnode=tarjanstack.pop()
                scc[popnode]=scccnt
                intarjanstack[popnode]=0
                if popnode==node:
                    break
            scccnt+=1
        yield 1
    for i in range(n):
        if dfn[i]==10**6:
            tarjan(i)
    #print(scc)
    cnt=Counter(scc)
    r=sum(1 for key in cnt if cnt[key]>1)
    print(r)
    #print(scc)

for i in range(1):
    solve()



