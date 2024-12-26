class BIT():
    def __init__(self,lenth):
        self.len=lenth
        self.tree=[0]*(lenth+1)
    def presum(self,i):
        r=0
        while i>0:
            r+=self.tree[i]
            i=i-(i&(-i))
        return r
    def dsum(self,l,r):
        return self.presum(r)-self.presum(l)
    def update(self,i,val):
        #if i==0
        while i<=self.len:
            self.tree[i]+=val
            i+=(i)&(-i)
