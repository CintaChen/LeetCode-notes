#一层一层削，可行但是时间复杂度高
# 首先双指针，分俩种情况，1、递增型，无法储水，我们会更新左右的max值；2、递减型，可以储水，按照最矮的计算（会不会漏解）error
# [5,1,2,3,4,5]
#
class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        left_max=height[0]
        right_max=height[-1]
        water_Sum=0
        while left<=right:#注意=，可能会漏解
            total_min=min(left_max,right_max)
            if total_min==left_max:
                if left_max<=height[left]:
                    left_max=height[left]
                    left+=1
                else:
                    water_Sum+=(left_max-height[left])
                    left+=1
            else:
                if right_max<=height[right]:
                    right_max=height[right]
                    right-=1
                else:
                    water_Sum+=(right_max-height[right])
                    right-=1
            
            
        return water_Sum

            





        