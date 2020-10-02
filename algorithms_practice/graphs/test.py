from collections import defaultdict
graph=defaultdict(list)

a=[[1,2], [1,3], [2,3]]
for i,v in a:
    graph[i].append(v)
    graph[v].append(i)
print(graph)
