# https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodes={}
        for edge in edges:
            if edge[0] not in nodes:
                nodes[edge[0]]=1
            else:
                nodes[edge[0]]+=1
            if edge[1] not in nodes:
                nodes[edge[1]]=1
            else:
                nodes[edge[1]]+=1
            
        
        for i in nodes:
            if nodes[i] == len(nodes)-1:
                return i  
        return -1

            

        
