#link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited={}
        listSubString=["",]
        index=0
        for i in range(len(s)):
            if s[i] not in visited:
                visited[s[i]]=i
                listSubString[index]+=s[i]
                       
            else:
                for key in visited:
                    if visited[key] < visited[s[i]]:
                        visited[key]=-1
                    
                visited[s[i]]=i  
                index+=1
                indexes=list(visited.values())
                stringSub=""
                indexes.sort()
                for i in indexes:
                    if i!=-1:
                        stringSub+=s[i]
                listSubString.append(stringSub)  
        
        return len(max(listSubString,key=len))
                    

            
                

        
