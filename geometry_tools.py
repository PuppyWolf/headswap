'''
2D  坐标采用  device coordinates ，左下角为原点,
如果是图片坐标系， 需要变换一次
'''

import math


# 计算直线的法线方向 这里line 用投影几何表示 [a,b,c]
def perpendcular_line(line, normalize= True, reverse= False):
    a , b ,c  = get_two_point_para_from_line (line )

    if normalize :
        m = math.sqrt( a**2 + b**2 )
        a /= m
        b /= m
    if reverse :
        return  [a, b , 1 ]
    return [-a, -b, 1]

# 2D point 按方向平移
def translate_point(point , direction , offset ):
    return [point[0] + direction[0]*offset , point[1] + direction[1]*offset]

# 直线垂直平移
def perpendicular_translate_line(line ,offset ):
    normal_ = perpendcular_line( line )
    new_p1  = translate_point(line[0] , normal_ , offset)
    new_p2 = translate_point(line[1], normal_, offset)
    return [new_p1 , new_p2]

# 将line = [ p1 , p2 ] 转为 两点式 [a,b,c ]
def get_two_point_para_from_line(  line ):
    p1  , p2 = line[0] , line[1]
    x1 , y1 =  p1[0] , p1[1]
    x2 , y2 =   p2[0] , p2[1]
    a =  y2 - y1
    b =  x1 - x2
    c = x2*y1 -  x1 * y2
    return [a,b,c ]


# 计算两直线的交点 , line1 用 [a1, b1,c1 ] 表示
def intersec_point(line1, line2 ):
    a1  , b1 , c1  = line1[0] , line1[1] , line1[2]
    a2, b2, c2 = line2[0], line2[1], line2[2]
    den  = a2 * b1  - a1* b2
    if den==0 :
        print(" 两直线平行，无交点")
        return None
    else :
        x = (b2*c1 - b1*c2) / den
        y = (a1*c2 - a2*c1 ) /den
    return [x,y]



#  计算lines 的偏移线 :  lines : [ [x1,y1] , ... ]
# 假设 lines 的第一个点 是 半开放点，即只连接一条线段
def line_segments_offset( lines , offset):
    n_points = len(lines)
    new_lines = []
    for i in range(n_points):
        if (i == 0) or (i == (n_points-1)):
            # 直接计算点位
            if i==0 :
                p1 = lines[0]
                p2 = lines[1]
                normal_ = perpendcular_line([p1, p2])
                new_point = translate_point(p1,normal_ ,offset )
            else :
                    p1  = lines[i -1]
                    p2 =  lines[i]
                    normal_ = perpendcular_line([p1, p2])
                    new_point = translate_point(p2, normal_, offset)
        else :
            # 通过直线交点计算点位
            line1 = [ lines[i-1] , lines[i]  ]
            line2 = [lines[i ], lines[i+1 ] ]
            line1_offset = get_two_point_para_from_line( perpendicular_translate_line(line1, offset) )
            line2_offset = get_two_point_para_from_line(perpendicular_translate_line(line2, offset))
            new_point  = intersec_point(line1_offset , line2_offset)

        new_lines.append(new_point)
    return new_lines


#  test
def tes_line_segment_offset():
    lines = [[50.0 , 50.0] , [70.0 , 70.0 ] , [90.0 , 50.0]]
    offset = 10
    line_segments_offset(lines , offset)


if __name__ == '__main__':
    tes_line_segment_offset()