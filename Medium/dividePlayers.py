#link: https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/?envType=daily-question&envId=2024-10-04

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i,j=0,len(skill)-1
        pairs=[]

        while(i<j):
            pairs.append((skill[i],skill[j]))
            i+=1
            j-=1  

        temp_total=sum(pairs[0])
        sumChemistry=0
        for pair in pairs:
            if sum(pair)!=temp_total:
                return -1  
            sumChemistry+=pair[0]*pair[1]

        return sumChemistry            
            
            
        

            


            

            
        


    


        
