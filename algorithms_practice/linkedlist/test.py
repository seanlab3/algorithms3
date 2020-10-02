class ListNodeSort:
    def __init__(self, x):
        self.val = x
        self.next = None
def printList(l):
    value = []
    while(l):
        value.append(l.val)
        l = l.next
    print(' -> '.join(map(str, value)))
alist=[4,5,6,3,45,6]

nodelist=[ListNodeSort(i) for i in alist]
for i in range(len(alist)-1):
    nodelist[i].next=nodelist[i+1]
printList(nodelist[0])

