def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def quad_area(s1, s2, s3, s4, d1, d2, d3, d4):
    a1 = triangle_area(s1, s2, d1)
    a2 = triangle_area(s2, s3, d2)
    a3 = triangle_area(s3, s4, d3)
    a4 = triangle_area(s4, s1, d4)
    return a1 + a2 + a3 + a4

s1, s2, s3, s4 = 5, 6, 7, 8  
d1, d2, d3, d4 = 2, 3, 4, 5  

area = quad_area(s1, s2, s3, s4, d1, d2, d3, d4)
print(area)
