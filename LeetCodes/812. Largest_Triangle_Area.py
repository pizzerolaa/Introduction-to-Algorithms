# Given an array of points on the X-Y plane points where points[i] = [xi, yi], 
# return the area of the largest triangle that can be formed by any three different points. 
# Answers within 10-5 of the actual answer will be accepted.

def largest_triangle_area(points: list[list[int]]) -> float:
    def area(p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        return 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
    
    max_area = 0
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                max_area = max(max_area, area(points[i], points[j], points[k]))
    return max_area

points = [[4,6],[6,5],[3,1]]
input()
print(largest_triangle_area(points))

#bro wth with this leetcode, it supposed this one is easy nahhh