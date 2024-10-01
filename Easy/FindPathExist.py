#Link https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source==destination:
            return True

        graph={}
        for i in range(n):
            graph[i]=[]  
        
        for edge in edges:
            graph[edge[0]].append(edge)
            graph[edge[1]].append(edge)

        stack={}
        visited={}
        stack[source]=None
        while(len(stack)!=0):
            u=next(iter(stack))
            del stack[u]
            visited[u]=None
            for edge in graph[u]:
                if edge[0] == destination or edge[1]==destination:
                    return True
                if edge[0] not in visited:
                    stack[edge[0]]=None
                elif edge[1] not in visited:
                    stack[edge[1]]=None
        return False

        

        



            


        



        
