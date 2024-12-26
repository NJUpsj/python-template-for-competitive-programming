import sys
def input(): return sys.stdin.readline().strip() # fast IO

def LII():
    return list(map(int, input().split())) #read list

# --------------------
# 手写栈模板
# 克服py栈太浅的问题
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

from  typing import *

def solve():

    n=int(input())
    dag=LII()
    dpls=[[] for i in range(n)]
    for i in range(n-1):
        dpls[dag[i]-1].append(i+1)
    nodesum=[0 for i in range(n)]

    @bootstrap
    def dfs_t(i):
        sum1=1
        for j in dpls[i]:
            sum1+=yield dfs_t(j)
        nodesum[i]=sum1
        yield sum1
    dfs_t(0)
    result=0
    @bootstrap
    def dfs(i,more):
        if nodesum[i]<=2:
            #return 0
            yield 0
        ls=[]
        for j in dpls[i]:
            ls.append(nodesum[j])
        ls.sort()
        sum1=nodesum[i]-1
        if sum1+more>=ls[-1]*2:
            yield (sum1-more)//2
        newmore=max(more+sum1-ls[-1]-1,0)
        for j in dpls[i]:
            if nodesum[j]==ls[-1]:
                index=j
                break
        yield (yield dfs(index,newmore))+sum1-ls[-1]
    result=dfs(0,0)
    print(result)


for _ in range(int(input())):
    solve()