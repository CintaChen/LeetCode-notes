#比较排序后的片段与原始片段，记录左指针位置
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left=0
        outcome=[]
        resort=sorted(p)
        for right in range(len(p)-1,len(s)):
            
            part=s[left:right+1]
            part_resort=sorted(part)
            if part_resort==resort:
                outcome.append(left)
            left+=1
        return outcome
# 改进：可以计算频率，避免无效的计算