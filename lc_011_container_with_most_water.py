class Solution:
    def maxArea(self, height: List[int]) -> int:
        def water_between_points(left_point, right_point):
            return (right_point-left_point) * min(height[left_point], height[right_point])
        left_point, right_point, res = 0, len(height) - 1, -1
        while left_point != right_point:
            res = max(res, water_between_points(left_point, right_point))
            if height[left_point] < height[right_point]: left_point += 1
            else: right_point -= 1
        return res
        
