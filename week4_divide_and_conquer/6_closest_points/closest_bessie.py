#Uses python3
import sys
import math
import random



class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return str([self.x,self.y])

def construct_point(x_list, y_list):
    return [Point(x_list[i], y_list[i]) for i in range(len(x_list))]

def distance_bessie(a, b):
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5

def calculate_small_region(points):
    if len(points) == 2:
        return distance_bessie(points[0],points[1])
    result = sys.maxsize
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            result = min(result, distance_bessie(points[i],points[j]))
    return result


def pre_process(x_list, y_list):
    points = construct_point(x_list, y_list)
    points = sorted(points, key=lambda a: a.x)
    return points

def minimum_distance_bessie(points):
     #sorted by the x-coordinates
    if len(points) <= 3:
        return calculate_small_region(points)
    mid = len(points)//2
    left_side_min_dis = minimum_distance_bessie(points[0:mid])
    right_side_min_dis = minimum_distance_bessie(points[mid:])
    min_dis_in_small_region = min(left_side_min_dis, right_side_min_dis)
    split_vertical_line = (points[mid-1].x + points[mid].x)/2


    suspicious_point = []
    #for the left part:
    for i in range(len(points[0:mid])):
         if abs(points[i].x - split_vertical_line)<=min_dis_in_small_region:
             suspicious_point.append(points[i])

    # for the right part:
    for i in range(len(points[mid:])):
         if abs(points[i+mid].x - split_vertical_line) <= min_dis_in_small_region:
             suspicious_point.append(points[i+mid])

    suspicious_point = sorted(suspicious_point, key = lambda a: a.y)
    result = min_dis_in_small_region
    for i in range(len(suspicious_point)):
        for j in range(i+1, min(i+8, len(suspicious_point))):
            if abs(suspicious_point[i].y - suspicious_point[j].y) <= result:
                result = min(result, distance_bessie(suspicious_point[i], suspicious_point[j]))

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = pre_process(x,y)
    print("{0:.9f}".format(minimum_distance_bessie(points)))