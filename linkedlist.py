"""class node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
a=node(1)
a.next=node(4)
c=a.next.next=node(9)
print(a,a.data,a.next.data,a.next.next.data)
print(a.next,c)"""
class node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=next
def insert(self,data):
    if head==None:
        self.head=node(1)
    else:
        new=node(data)
        new.next=self.head
        self.head=new
    def printing(self):
        if self.head==None:
            return
        i=self.head
        while i:
            print(i.data)
            i=i.next

l=[1,2,3,4,5]
head=None
for i in l:
    insert(i)
    head.printing()
    
